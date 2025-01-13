# **V-Secure**: An Intelligent Data-Driven Model to Secure Intra-Vehicle Communications 🚗🛡️

## Overview

This project aims to secure intra-vehicle communications using a dual-layer model combining image-based and data-based approaches. By leveraging deep learning and structured data analysis, the system can effectively detect and prevent cyber threats, ensuring robust vehicle network security.

## Demo Video



<video src="https://github.com/user-attachments/assets/554c3838-c8cc-48d8-934f-0366bc5347c1" width="352" height="720"></video>
## Features

### Image-Based Model

![Image-Based Model Visualization](all%20img.png)
![Image-Based Model Visualization](all%20img2.png)

- **Pattern Recognition in Visual Data:** Utilizes deep learning to analyze visual representations of network activity, such as CAN bus signal patterns or heatmaps, to detect unusual shapes or spikes that may indicate cyber threats.
- **Enhanced Detection of Anomalies:** Identifies deviations in normal waveform patterns to spot attacks that alter typical signal flow, such as spoofing or injection attacks.

### Data-Based Model

- **Structured Data Analysis:** Processes network data (e.g., frequency, timing, and sequence of sensor readings and messages) to detect irregularities that could signal attacks like Man-in-the-Middle (MITM) or Denial of Service (DoS).
- **Adaptable to Data Types:** Can analyze various structured data points from different Electronic Control Units (ECUs), allowing for a versatile approach across multiple vehicle components and communication protocols.

### Integrated Dual-Layer Security

- **Cross-Model Validation:** Combines outputs from both models to strengthen accuracy and minimize false positives, ensuring comprehensive detection across image and structured data.
- **Robust Against Complex Attacks:** Capable of detecting both visual and non-visual anomalies, covering a wide range of potential intra-vehicle threats.

## Common Cyber Threats

- **Fuzzy Attack:** A cybersecurity testing method where random, malformed, or unexpected data is fed to software, systems, or devices to identify vulnerabilities and weaknesses.
- **Denial of Service (DoS) Attacks:** Overloads the vehicle network with false data to disrupt essential functions like braking or steering control.
- **Spoofing Attacks (RPM and Gear):** Injects false signals or messages into the network, impersonating legitimate components to mislead the vehicle system.

## Detection Challenges

- **Subtle, Low-Signal Attacks:** Sophisticated attackers often create small, unnoticeable anomalies, which are hard to distinguish from normal fluctuations in high-speed data flows.
- **High Data Volume:** Vehicle networks generate and exchange massive amounts of data in real-time, making it difficult to identify attacks without causing system delays.
- **Time-Sensitive Processing:** Attack detection must happen instantly to be effective, requiring highly optimized algorithms that balance security with processing speed.

## Image-Based Models

| MODEL NAME       | ACCURACY |
| ---------------- | -------- |
| CNN              | 0.9762   |
| XCEPTION         | 1.00     |
| VGG16            | 0.9989   |
| VGG19            | 1.00     |
| RESNET           | 0.98     |
| INCEPTION        | 0.9996   |
| INCEPTION RESNET | 0.9999   |

## Data-Based Models

| MODEL NAME          | ACCURACY |
| ------------------- | -------- |
| Logistic Regression | 0.9957   |
| KNN                 | 0.9999   |
| Random Forest       | 1.00     |

## Technologies Used

- **Programming Language:** Python
- **Deep Learning Frameworks:** TensorFlow, PyTorch
- **Visualization Tools:** Matplotlib, Seaborn
- **Dataset:** Car Hacking  Dataset
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Rijul1607/V-Secure.git
   ```
2. Navigate to the project directory:
   ```bash
   cd V-Secure
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Data Preprocessing:** Use the provided scripts to preprocess both image and structured data.
2. **Model Training:** Train the image-based and data-based models using the preprocessed data.
3. **Real-Time Monitoring:** Deploy the dual-layer model for real-time intra-vehicle communication monitoring.

## DataSet

Access the DataSet here: [Database Repository](https://github.com/Rijul1607/V-Secure/tree/main/dataset)


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or inquiries, please contact [Rijul](mailto:your.email@example.com).

