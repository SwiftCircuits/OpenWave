# OpenWave: Precision Arbitrary Waveform Generator

<div align="center">

[![License: CERN-OHL](https://img.shields.io/badge/Hardware-CERN--OHL-yellow.svg)](https://ohwr.org/cernohl)
[![License: MIT](https://img.shields.io/badge/Software-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Project Status: WIP](https://img.shields.io/badge/Project%20Status-WIP-orange.svg)]()

**A dual-channel, high-precision waveform generator designed for control system analysis and system identification**

[Features](#features) • [Getting Started](#getting-started) • [Documentation](#documentation) • [Contributing](#contributing)

<img src="/docs/Logov1Wide.png" alt="OpenWave Project Banner">

</div>

## Why OpenWave?

Traditional arbitrary waveform generators often force a choice between expensive lab equipment or limited-capability hobby projects. OpenWave bridges this gap by providing professional-grade precision in an open-source design that prioritizes signal quality over raw speed. By focusing on the critical frequency range used in control systems and system identification (up to 500 kHz), we've optimized for exceptional signal quality and reliability.

### Key Features

- Dual independent channels with 16-bit resolution
- Optimized 500 kHz bandwidth with 80 dB SNR
- Sophisticated triggering system for precise control
- Multiple interface options: USB, Ethernet, and CAN
- Intuitive front panel control with LCD display
- Expansion capability through daughter board interface
- Precision temperature-monitored reference system
- Professional-grade signal filtering and conditioning

### Perfect For

- Control system development and testing
- System identification experiments
- Precision measurement applications
- Educational laboratory setups
- Research and development projects
- Industrial control system integration
- Signal processing development

## Technical Overview

OpenWave combines meticulous hardware design with flexible software to achieve exceptional signal quality:

### Signal Generation
- Dual 16-bit DACs (LTC2642-16) operating at 50 MSPS
- Third-order Sallen-Key filtering with Butterworth response
- Additional output stage conditioning
- Ultra-low noise power supply design
- Temperature-compensated reference system
- Comprehensive signal isolation and protection

### Control and Interface
- High-speed USB 2.0 interface
- 10/100 Ethernet connectivity
- Industrial-grade CAN interface
- Advanced trigger system with multiple modes:
  - Start trigger with precise timing
  - Level-sensitive pause control
  - Configurable burst mode
  - Status and peak detection outputs
- Intuitive front panel interface with LCD display

### Power System
- 12V DC input with protection
- Sophisticated multi-stage power architecture:
  - High-efficiency 5.5V pre-regulation
  - Ultra-low noise 5V analog supply
  - Clean 3.3V digital rail
  - Precision 3.3V reference
- Extensive power filtering and isolation

## Getting Started

### Current Status
This project is under active development. Current focus areas:
- Finalizing PCB layout and power distribution
- Implementing core firmware features
- Developing user interface systems
- Creating comprehensive documentation
- Establishing test procedures

### For Contributors

We welcome contributions in several areas:

**Hardware Development**
- PCB layout optimization
- Signal integrity improvements
- Power distribution refinement
- Manufacturing optimization
- Test coverage enhancement

**Firmware Development**
- STM32 core implementation
- Front panel interface development
- Communication protocol implementation
- Signal generation algorithms
- User interface refinement

**Documentation and Testing**
- System specification documentation
- Assembly and calibration procedures
- Performance verification methods
- Application examples
- User manual development

## Building OpenWave

### Hardware Requirements
- 4-layer PCB manufacturing capability
- SMD assembly equipment
- Precision test equipment:
  - Oscilloscope (>100MHz bandwidth)
  - Precision multimeter
  - Signal analyzer (recommended)
- STM32 programming capability
- Basic electronic assembly tools

### Software Requirements
- STM32CubeIDE development environment
- ARM GCC toolchain
- KiCad 7.0 or later
- Git version control
- Build system requirements (detailed in documentation)

## Documentation

> 🚧 Documentation is currently under development

Comprehensive documentation will cover:
- Complete system architecture
- Detailed theory of operation
- Assembly and testing procedures
- Calibration methodology
- Performance optimization
- Application examples
- Development guidelines

## Contributing

Your expertise can help make OpenWave better! Here's how you can contribute:

1. **Join Discussions**
   - Share your application requirements
   - Suggest performance improvements
   - Help define future features
   - Participate in design reviews

2. **Technical Contributions**
   - PCB design optimization
   - Firmware development
   - Documentation creation
   - Test procedure development
   - Performance validation

3. **Testing and Validation**
   - Prototype building and testing
   - Performance verification
   - Use case validation
   - Issue reporting and tracking

## Project Structure

```
/hardware           - KiCad design files
  /main            - Main board design
  /front_panel     - Front panel PCB
  /daughter_boards - Expansion board designs
  /manufacturing   - Production files
/firmware          - Source code
  /core            - Core STM32H7 functionality
  /front_panel     - STM32G0 interface code
  /libraries       - Shared libraries
  /tests           - Test suites
/docs              - Documentation
  /hardware        - Hardware documentation
  /firmware        - Software documentation
  /user            - User guides
  /testing         - Test procedures
```

## License

- Hardware: [CERN Open Hardware License Version 2](LICENSE-HARDWARE)
- Software: [MIT License](LICENSE-SOFTWARE)

## Acknowledgments

OpenWave builds on the work of many open-source projects and individuals. Special thanks to:
- The open hardware community for inspiration and shared knowledge
- Contributors who have helped shape the project's direction

## Contact and Support

- Create an issue for bugs or feature requests
- Join our discussions for general questions
- Email for other inquiries: constantinescu.alex02@gmail.com

---

<div align="center">

**[Back to Top](#openwave-precision-arbitrary-waveform-generator)**

</div>
