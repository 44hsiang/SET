from zhinst.qcodes import ZISession 

def basic_mfli_setup(mfli, V_exc, frequency):
    OUT_CH   = 0  
    OSC      = 0   
    DEMOD    = 0  # demodulator 1 

    with mfli.set_transaction():
        # Output setup             
        mfli.sigouts[OUT_CH].on(True)
        mfli.sigouts[OUT_CH].enables[1].value(True)

        # Set output amplitudes for both paths
        mfli.sigouts[OUT_CH].amplitudes[1].value(V_exc)    
        
        # Set frequency of oscillator
        mfli.oscs[OSC].freq(frequency)  # Set frequency
        
        # Input setup
        mfli.sigins[0].range(0.1)  # This may need to be adjusted based on the input signal
        mfli.demods[DEMOD].enable(True)
        mfli.demods[DEMOD].oscselect(OSC)
        mfli.demods[DEMOD].adcselect(0)
        mfli.demods[DEMOD].order(4)
        mfli.demods[DEMOD].timeconstant(0.01)

    return mfli

if __name__ == "__main__":
    mfli_addr = "192.168.0.220"
    DEVICE_ID = "dev30577"
    session = ZISession(mfli_addr)
    device = session.connect_device(DEVICE_ID)
    print("Connected to device:", device.name)
    basic_mfli_setup(device, V_exc=0.1, frequency=1e3)
    print("MFLI setup Vexc 0.1 and frequency 1 kHz.")
    print("Finished setting up MFLI device.")