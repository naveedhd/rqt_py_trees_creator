cmake_minimum_required(VERSION 2.8.3)
project(rqt_py_trees_creator)
set(CMAKE_CXX_FLAGS "-g ${CMAKE_CXX_FLAGS}")

# Load catkin and all dependencies required for this package
find_package(catkin REQUIRED)
catkin_package()
catkin_python_setup()

install(FILES plugin.xml
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(PROGRAMS scripts/rqt_py_trees_creator
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)