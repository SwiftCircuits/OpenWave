# 2025
## February
### 18
1. Started with ambitious specs: 30MHz, 8-10 bit, dual-channel AWG
2. Initial architecture: Parallel DAC (MCP4922) and external SRAM (23LC1024)
3. After analysis, found serious implementation challenges:
    - Parallel interface requires complex timing and many GPIO lines
    - Memory bandwidth requirements extremely high (3 Gbps)
    - Output stage needs expensive high-speed op-amps
4. Strategic compromises for first prototype:
    - Reduced target to 5MHz while maintaining SNR goals (60 dB)
    - Switched to SPI DAC (LTC2642 at 50 MSPS)
    - Using MCU internal RAM instead of external SRAM
    - Selected LMH6658 op-amp 
    - Added physical controls for standalone operation
5. Design simplifications without compromising core functionality:
    - MCU internal comparators for trigger system
    - Double buffering scheme in MCU RAM
    - Focused on 50Ω load capability
    - Added CAN for future expansion
    - Removed battery backup functionality to reduce complexity
    - Switched from USB power to 12V input for better power budget
6. Power Architecture Refinement:
    - Implemented three-stage power system:
        - 12V to 5V switching (TPSM863252)
        - Separate 3.3V analog/digital LDOs
        - Precision 3.3V reference (REF3333)
    - Accepted slightly higher noise on analog supply (TPS70933DBVR) after analyzing complete signal chain
7. Selected Core Components:
    - STM32H743VIT6 MCU (480MHz, 1MB RAM)
    - LTC2642 12-bit DAC
    - LMH6658 Op-amp
    - REF3333 Voltage Reference

Current Implementation Path:

- Revised specs to 5MHz with 60 dB SNR/THD
- First prototype focusing on reliable operation
- Added practical features (standalone operation, CAN)
- Designed for realistic hobbyist manufacturing
- Structured power system for clean signal generation
- Clear subsystem testing strategy:
    1. Power supply validation
    2. Digital section
    3. DAC interface
    4. Analog output stage
- Left upgrade paths for future performance improvements

Engineering Notes:

- Power budget calculations show ~5-7W total system draw
- Analyzed noise chain through power supplies and op-amp
- Memory requirements well within MCU capabilities
- Digital current draw estimated at ~250mA worst case
- Temperature considerations for voltage reference critical
### 19

#### Key Decisions
- Stepped requirements down to 2MHz
- Decided to use PCBs for Front and Back Panels

#### Daily TODO

- [ ]  Complete STM32CubeIDE basic setup
- [x]  Start power distribution schematic
- [x]  Research mixed-signal board layout guidelines

#### End of Day Notes

- Schematic done around STM32 and Power System
- Changed power arhitecture, now stepping 12V down to 5.5V which is split across the 2 LDOs and the VRef generator, one of the LDOs now is a fixed 5V one with filtering (for better DAC/OpAmp Performance)
  

#### Tasks

1. STM32CubeIDE Project Setup
    
    ##### Progress
    
    - HSE configured at 25 MHz
    - Clock configuration auto-solved
    - SWD debugging enabled
    - Enabled peripherals:
        - FDCAN
        - SPI
        - QSPI: Bank 1 with Quad SPI Lines
        - USB_OTG_FS - Device - CDC
    
    ##### TODO
    
    - [ ]  Optimize clock tree configuration
    - [ ]  Complete DMA setup
    - [x]  Review USB device class options
    
    ##### Issues
    
    - [x]  ~~RCC CRC SYNC confusion~~
        - Solution: This is CRS_SYNC (Clock Recovery System)
        - Used for USB SOF synchronization
    - [x]  ~~PWR Monitoring State~~
        - Solution: Always active, UI toggle for external only
    - [x]  ~~USB VBUS handling~~
        - Solution: PA9 with voltage divider
    
    ##### Notes
    
    - Clock auto-configuration creates too many divisions
    - May need to revisit USB configuration for custom device class
    - DMA priority scheme needs careful consideration
2. Schematic Design
    
    ##### Progress
    
    - Started STM32H743VIT6 section
    - Added backup battery circuit
    
    ##### TODO
    
    - [x]  Review crystal layout requirements
    
    ##### Notes
    
    - VBat connected through solder jumper
    - Consider adding test points for power rails

#### References

- STM32H743 Reference Manual
- AN4950: Crystal oscillator configuration
- Mixed-signal PCB design guidelines
### 20

#### Key Decisions
- Reduced Battery to 20 mm size - 30 is too much!
- Decided that front panel will have dedicated extremely low cost STM32 to handle I/O
- Related to above, decided on a simple LCD Screen.

#### Today's Goals
- [ ] Finish up most of the core schematic
- [ ] Review Core Schematic

#### Tasks

1. Schematic
    ##### TODO
    - [x] Fix step-down divider to get 5.5V instead of 5V
    - [ ] Add debug options ( Test Points, LEDs, UART )
    - [x] Add CAN
    - [x] Connect everything to the STM after initial layout considerations
    
    ##### NOTES
    - After hours of intense thought, decided to keep current DAC with only 2 MHz usable and 12 bit due to simplicity in this initial version

#### End of Day Notes
- Finished V0.1 of Schematic with connections
- Decided I must learn to simulate filter response and design.

#### Gallery
![[OpenWave_Init.pdf]]
- Caption: Init version of full Schematic

### 22

Extra note: Spend 21 and most of 22 learning Simscape and Simulink to simulate some filters
#### Key Decisions
- Decided to implement 3rd order Sallen-Key with Butterworth response on the output from the DAC.

#### Today's Goals
- [ ] Finish filter design and implementation

#### Tasks

1. Filter
    ##### TODO
    - [ ] Consult with mentor on ideal power filter cut-off freq
    
    ##### NOTES
    - Basically filtering anything above 850 kHz. I love it how I started with 20 MHz in plan haha
    


#### End of Day Notes
- Made a filter
  - Essential for proper output

#### Gallery
![[OutputFilterResponse.png]]
- Caption: Output Filter Response
![[OutputFilterDesign.png]]
- Caption: Output Filter Design
![[PowerFilterResponse.jpg]]
- Caption: Power Filter Response