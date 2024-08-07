## Bridging the Gap: Digital Twin Integration and Evaluation in Robotic Multi-Axis Additive Manufacturing ##

This repository contains files for the paper titled "Bridging the Gap: Digital Twin Integration and Evaluation in Robotic Multi-Axis Additive Manufacturing," with Tomáš Jochman as the main author.


This study explores integrating digital twin technology with robotic multi-axis additive manufacturing to improve manufacturing precision and efficiency. A laser tracker calibrates the machine workspace and tools, incorporating an industrial robot with a filament extruder head and a rotary-tilt positioner. The digital twin captures the details of the manufacturing process and automates code generation for robotic operations. The method's effectiveness is shown through the production of two complex parts, assessing their dimensional accuracy to evaluate the technology's limits and potential. The results show substantial improvements in aligning virtual models with physical objects, demonstrating the digital twin's ability to reduce common deviations in traditional manufacturing.

# Project Contents

- **Robot Files:** KRL codes for the robotic controller.
- **NX Siemens Files:** Simulation of robotic paths and scans of printed parts in NX Siemens.
- **Laser Tracker - Raw data:** Raw data from laser tracker from measuring the printing pad and robot motion.
- **Python Files:** Scripts for visualizing the bilinear interpolation of the printing pad and visualization of the real robot paths from:
  1. Laser tracker measuring
  2. Virtual robot controller
  3. Real robot controller
  4. CAM - NX Siemens

# Key Features

- **Digital Twin Integration:** The study successfully integrates a digital twin (DT) with robotic multi-axis additive manufacturing, enhancing manufacturing precision and efficiency by bridging virtual planning with physical execution.
- **Laser Tracker Utilization:** A laser tracker is employed to calibrate the machine workspace and tools, introducing a system that combines an industrial robot with a filament extruder head and a rotary-tilt positioner.
- **Automated Code Generation:** The digital twin automates the generation of robotic operation codes, encapsulating the geometric and operational intricacies of the manufacturing process.
- **Demonstration through Complex Parts:** The methodology's application is demonstrated through the production of two complex parts, assessing their dimensional fidelity to evaluate the precision limits of digital twin technology.

# Video
<iframe width="560" height="315" src="https://youtu.be/Vr6lDgBZacE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<video width="320" height="240" controls>
  <source src="https://youtu.be/Vr6lDgBZacE" type="video/mp4">
  Your browser does not support the video tag.
</video>

[![Watch the video](https://img.youtube.com/vi/Vr6lDgBZacE/0.jpg)](https://youtu.be/Vr6lDgBZacE)
