from qcodes.dataset.data_set import load_by_id

class AxisInfo:
    def __init__(self, name, data, label=None, unit=None):
        self.name = name
        self.data = data
        self.label = label or name
        self.unit = unit or ""

    def __repr__(self):
        return f"<AxisInfo: {self.label} [{self.unit}] shape={self.data.shape}>"


class ParameterWrapper:
    def __init__(self, name, data, label="", unit="", dim=None, x=None, y=None):
        self.name = name
        self._data = data
        self.label = label
        self.unit = unit
        self.dim = dim
        self.x = x  # AxisInfo or None
        self.y = y  # AxisInfo or None

    @property
    def data(self):
        return self._data  # direct access to raw numpy array

    def full_label(self):
        return f"{self.label} [{self.unit}]" if self.unit else self.label

    def __repr__(self):
        return f"<Parameter: {self.label} [{self.unit}], dim={self.dim}>"

class QCoDeSDatasetWrapper:
    def __init__(self, run_ID):
        self.dataset = load_by_id(run_ID)
        self.ds_xarray = self.dataset.to_xarray_dataset()
        self._parse_parameters()

    def _parse_parameters(self):
        for par in self.dataset.get_parameters():
            if par.depends_on == '':
                continue

            depends = par.depends_on_
            name = par.name
            label = par.label
            unit = par.unit
            data = self.ds_xarray[name].to_numpy()

            x = y = None

            if len(depends) >= 1:
                x_name = depends[0]
                x_data = self.ds_xarray[x_name].to_numpy()
                x_param = next(p for p in self.dataset.get_parameters() if p.name == x_name)
                x = AxisInfo(x_name, x_data, x_param.label, x_param.unit)

            if len(depends) == 2:
                y_name = depends[1]
                y_data = self.ds_xarray[y_name].to_numpy()
                y_param = next(p for p in self.dataset.get_parameters() if p.name == y_name)
                y = AxisInfo(y_name, y_data, y_param.label, y_param.unit)

            dim = len(depends)
            param_obj = ParameterWrapper(name, data, label, unit, dim, x, y)
            setattr(self, name, param_obj)

            # Print info
            dim_str = f"{dim}D" if dim <= 2 else f"{dim}D (not fully supported)"
            print(f"→ Parsed {dim_str} parameter: {name}, depends on: {depends}")
