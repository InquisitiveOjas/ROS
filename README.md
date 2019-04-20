# ROS
Learning attempt on Robot Operating System.

ROS NODES: Data/Information processing software units.Provides modularity in big projects.

ROS TOPICS: Entities that transport information between nodes.Topic is identified by name and type.

Information is organised as a data structure [strings,integers,floating point numbers]

Important building blocks of a ROS application:
                                                  
(1)Publisher Nodes:-A ROS node that generates information is called a publisher. A publisher sends information to nodes via topics.      With robotics often these publishers are connected with sensors like cameras, encoders etc..
If you use the rosnode info command you can see with which topics a node is connected and if these are outbound or inbound connections.           

(2)Subscriber Nodes:-A ROS node that receives information is called a subscriber. It's subscribed to information in a topic and uses      topic callback functions to process the received information.
With robotics, subscribers typically monitor system states such as triggering an alert when the robot reaches joint limits.

A subscriber callback function processes the data from a topic it subscribes to only when a new data is published.

ROS FILE SYSTEM:
ROS workspace (catkin workspace) consists of different subspaces. A workspace is a folder to organize ROS project files.                ROS uses catkin, which is a build tool to compile source files into binary files. Your code goes into the src workspace folder and  catkin manages the other ones. 
                
       
A catkin ROS workspace contains three main spaces:

    src space: contains source code, this will be your main work folder
    
    devel space: contains setup files for the project ROS environment
    
    build space: contains the compiled binary files
    
First, create a new folder for your workspace:
        
    $ mkdir -p new_ros_ws/src

You can use the ls command to verify the new folder that was created.

Next move to your newly created workspace using the command:
      
    cd new_ros_ws.

Thereafter, setup the correct ROS environment using the command: 

    source /opt/ros/kinetic/setup.bash. 
Finally, we initialize catkin:

    $ catkin init
    $ catkin build


ROS packages reside in the 'src' space. In ROS, software is organised in ROS packages. A ROS package typically contains the following things:
      
      - CMakeList.txt
      - package.xml (These two files indicate that the folder is a ROS package file.)
      - scripts/ (This folder contains all Python scripts.)
      - src/ (This folder contains all C++ source files)
      
To create a new ROS package, we will use catkin:

      $ cd <path_to_ros_ws>/src
      $ catkin_create_pkg hrwros_week2 std_msgs
      
We can simply install their binaries with the rosdep command:

      $ rosdep install <package_name>

You can also install all ROS package dependencies in one command:

      $ cd <path_to_ros_ws>/src
      $ rosdep install --from_paths . --ignore-src -y
      
src is not the only space in your workspace: there is also the 'devel' space. This contains all binary executables from your src spaces.

Topic type is an abstract idea that acquires or inherits the ROS message type that is to be exchanged between nodes.

ROS also supports derived message types.

Nodes can process and share information through topics. The information they pass through these topics needs to be structured in some way, to make it actually usable. Such a structure is known as a data structure. In ROS, we can abstract these data structures as ROS message types. Common data structures in ROS are for example floats, integers, and strings.

In ROS, we can easily combine multiple data structures using derived message types. For example, to represent a position in 3D space we will need 3 floating point values: X, Y and Z. The derived message type will then be a struct of three floating point numbers: {float x, float y, float z}.

These (derived) message types are defined in message files. These message files are typically located in <ros_package_name>/msg, with the filename <NewMessageType>.msg.
  
