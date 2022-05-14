#!/usr/bin/env python
import  rospy
import  os
import roslaunch
import  time 

#f = open(os.path.dirname(__file__) + '/../world/test.world', "w")
f = open(os.path.split(os.path.dirname(__file__))[0] + '/world/test.world', "w")
print(os.path.split(os.path.dirname(__file__))[0] + '/world/test.world')
robots=rospy.get_param("/swarm/robots")
print(robots)
if (robots == None):
     ROS_ERROR("Error in getting the robots param\n");

f.write("""define block model
(
  size [20 0.5 0.5]
  gui_nose 0
)
define block1 model
(
  size [1 1 1]
  gui_nose 0
)

define topurg ranger
(
  sensor(       
    range [ 0.0  4.5 ]
    fov 360
    ranger_return 1.0
   samples 360
  )

  # generic model properties
  color "black"
  size [ 0.05 0.05 0.1 ]
)
define topurg1 ranger
(
  sensor(       
    range [ 0.0  4.5 ]
    fov 360
    ranger_return 1.0
   samples 360
  )

  # generic model properties
  color "black"
  size [ 0.05 0.05 0.1 ]
)

define erratic position
(
  #size [0.415 0.392 0.25]
  size [0.25 0.25 0.25]
  ranger_return 1.0
  origin [-0.05 0 0 0]
  gui_nose 1
  drive "diff"
  odom_error [0.0 0.0 0.00 0.0]
  topurg(pose [ 0.050 0.000 -0.2 0.000 ])
  topurg1(pose [ 0.050 0.000 0 0.000 ])
)

define floorplan model
(
  # sombre, sensible, artistic
  color "gray30"

  # most maps will need a bounding box
  boundary 1

  gui_nose 0
  gui_grid 0

  gui_outline 0
  gripper_return 0
  fiducial_return 0
  ranger_return 1
)

# set the resolution of the underlying raytrace model in meters
resolution 0.02

interval_sim 100  # simulation timestep in milliseconds


window
( 
  size [ 745.000 448.000 ] 

  rotate [ 0.000 -1.560 ]
  scale 28.806 
)

block( pose [ 0 10 0 0 ] color "black")
block( pose [ 10 0 0 90 ] color "black")
block( pose [ 0 -10 0 0 ] color "black")
block( pose [ -10 0 0 90 ] color "black")
block1( pose [ 3.5 2.5 0 0 ] color "black")
block1( pose [ -3.5 2.5 0 0 ] color "black")
block1( pose [ 3.5 -2.5 0 0 ] color "black")
block1( pose [ -3.5 -2.5 0 0 ] color "black")
block1( pose [ 5.5 6.5 0 0 ] color "black")
block1( pose [ -5.5 6.5 0 0 ] color "black")
block1( pose [ 5.5 -6.5 0 0 ] color "black")
block1( pose [ -5.5 -6.5 0 0 ] color "black")



""")


for i in range(robots):
  f.write("erratic( pose [  "+str(i)+'  0 0  0] name "era'+str(i)+'" color "blue")\n')


