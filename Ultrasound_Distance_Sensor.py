//We want to construct a new message type called SensorInformation. It should contain:

//A ROS message type for interfacing with distance sensors

//A string containing the manufacturer name

//An unsigned integer containing the sensor part number

//We would create the following file: $HOME/hrwros_ws/src/hrwros_msgs/msg/SensorInformation.msg. It will contain the following:

sensor_msgs/Range sensor_data
string maker_name
uint32 part_number
