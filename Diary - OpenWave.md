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
1. Laying out major components:
   - 
  