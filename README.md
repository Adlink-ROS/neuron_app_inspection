# Neuron APP: Inspection

# Support Platform:

* ADLINK Controller:
  - ROScube-I
  - ROScube-X
  - ROScube starterkit
* ROS version:
  - ROS 2 foxy

# Usage

## Quickstart

1. Click application in Neuron App to open workspace. **Click Auto-inspection.**  It will build the resource at first time it's opened.
     ![](readme_resource/open_app.png)
   
2-1. Click "packages" on the right side.

2-2. Open list by click "RESOURCES" -> "user-workspace" -> "napp_inspction"
     ![](readme_resource/click_resource_inspec.png)
     

***NOTE!!! Following instruction would need : Right click desired launch file and click "Run" -> "Run Launch File" as image bellow***

   ![](readme_resource/launch_inspec.png)
     

3. Launch Navigation and image_saver as well as Rviz, choose **ONE**  file to launch: 

    * Simulation with Gazebo. It will open with default mememan map: **Launch gazebo_inspection.launch.py**
    
    **NOTE : Before you deploy inspection on Neuronbot2, you shall first complete [SLAM](https://github.com/H-HChen/neuron_app_slam) and [modify checkpoints](#inspection-on-custom-checkpoint).**

    * Deploy on Neuronbot2: **Launch neuronbot_inspection.launch.py**

4. Launch Behavior Tree and camera snapshot. **Launch bt_inspection_snapshot.launch.py**

    The robot will go through 3 checkpoint and take a photo at each point.

    ![](readme_resource/bt_demo.gif)
    
 ## Inspection on custom checkpoint

1. Launch Navigation 

    **NOTE: It will open with default map, please [modify launch file](https://github.com/H-HChen/neuron_app_navigation#navigation-on-custom-map) if you want to navigate on custom map.**
    * Simulation with Gazebo: **Launch gazebo_inspection.launch.py**
    * Deploy on Neuronbot2: **Launch neuronbot_inspection.launch.py**

2. Set goal in Rviz2 and record position of robot.

    After robot reached the goal, open the list left side with double click.
   
   **TF -> Frames -> base_link -> positoin , orientation**
   
   Record X, Y in positoin and Z, W in orientation.
   ![](readme_resource/inspect_rviz.png)


3. Click "Explorer" on the left side.

4. Open xml file.
    
    Click "src" -> "BT_ros2" -> "bt_xml" -> "neuronbot_inspection_snapshot.xml"

    
5. Modify robot checkpoint at value in SetBlackboard.

   fill in the property with " X ; Y ; Z ; W " format
   ![](readme_resource/modify_point.png)

   
   **NOTE: If you want to change xml file that launch file include, please modify file name in bt_inspection_snapshot.launch.py.**
   

6. Follow Step3 and Step4 in **Quickstart**.
