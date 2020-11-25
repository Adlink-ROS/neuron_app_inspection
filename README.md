# Neuron APP: Inspection

# Support Platform:

* ADLINK Controller:
  - ROScube-I
  - ROScube-X
  - ROScube starterkit
* ROS version:
  - ROS 2 foxy

# Usage
1. Click application in Neuron App to open workspace. **Click AUTO-inspction.**  It will build the resource at first time it's opened.
     ![](readme_resource/open_app.png)
   
2-1. Click "packages" on the right side.

2-2. Open list by click "RESOURCES" -> "user-workspace" -> "napp_inspction"
     ![](readme_resource/click_resource_inspec.png)
     

***NOTE!!! Following instruction would need : Right click desired launch file and click "Run" -> "Run Launch File" as image bellow***

   ![](readme_resource/launch_inspec.png)
     

3. Launch Navigation as well as Rviz with the Gazebo simulation. **Launch gazebo_inspection.launch.py**

    It will open with default mememan map. 

4. Launch Behavior Tree and camera snapshot. **Launch bt_inspection_snapshot.launch.py**

    The robot will go through 3 checkpoint and take a photo at each point.

    ![](readme_resource/bt_demo.gif)
    
* ### if you want to change checkpoint of Inspection, follow instruction bellow:

1. Launch Navigation and gazebo. **Launch gazebo_inspection.launch.py**

2. Set goal in Rviz2 and record position of robot.

    After robot reached the goal, open the list left side with double click.
   
   **TF -> Frames -> base_link -> positoin , orientation**
   
   Record X, Y in positoin and Z, W in orientation. Then you shall turn off Navigation.
   ![](readme_resource/inspect_rviz.png)


4. Click "Explorer" on the left side.
5. Click "src" -> "BT_ros2" -> "bt_xml" -> "bt_nav_mememan_snapshot.xml"
6. Modify robot checkpoint at value in SetBlackboard.

   fill in the property with " X ; Y ; Z ; W " format
   ![](readme_resource/modify_point.png)
