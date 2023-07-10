# Robotic-Vision-System

The Robotic Vision System project is a basic implementation of a vision system using Python and OpenCV. The system focuses on object detection and tracking through color-based segmentation.

## Summary

The goal of this project is to develop a computer vision system for robotic applications that can perceive and interact with objects in its environment. By leveraging OpenCV and Python, the system performs real-time detection and tracking of objects based on their color.

## Key Features

- Object detection: The system uses color-based segmentation to identify objects of interest in a video stream.
- Object tracking: Once an object is detected, the system tracks its movement across subsequent frames.
- Real-time processing: The system processes video frames in real-time, providing immediate feedback on detected objects.

## Usage

To use the Robotic Vision System:

1. Clone the repository: `git clone https://github.com/markwassef/Robotic-Vision-System.git`
2. Navigate to the project directory: `cd Robotic-Vision-System`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Run the robotic vision system: `python src/main.py`
5. The system will open a video stream from your default camera and detect blue objects in real-time. Press 'q' to exit.

## Customization

The system can be customized to detect objects of different colors. Modify the `lower_blue` and `upper_blue` variables in `main.py` to adjust the color range for object detection.

## Future Enhancements

While this project serves as an introductory implementation of a robotic vision system, there are several potential enhancements to consider:

- Object recognition using deep learning models for more accurate and versatile object detection.
- Integration of additional sensors or cameras for a richer perception of the environment.
- Implementation of advanced tracking algorithms to handle occlusions and object interactions.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
