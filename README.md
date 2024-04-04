<h1 align="center">Robotics 2: Forward and Inverse Kinematics of a Cylindrical Manipulator</h1>
<br>

## Table of Contents
  * [I. Abstract](#i-abstract)
  * [II. Introduction](#ii-introduction)
  * [III. Degrees of Freedom](#iii-degrees-of-freedom)
  * [IV. Kinematic Diagram and D-H Frame](#iv-kinematic-diagram-and-d-h-frame)
  * [V. D-H Parametric Table](#v-d-h-parametric-table)
  * [VI. Homogeneous Transformation Matrix](#vi-homogeneous-transformation-matrix)
  * [VII. Inverse Kinematics](#vii-inverse-kinematics)
  * [VIII. Forward and Inverse Kinematics Calculator (Application)](#viii-forward-and-inverse-kinematics-calculator-application)
  * [IX. References](#ix-references)
  * [X. Group Members](#x-group-members)
<hr> 
<br>


## I. Abstract
<p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This study presents a thorough examination of the forward and inverse kinematics of cylindrical manipulators, providing valuable insights on their fundamental principles and practical applications. By establishing the relationships between joint parameters and end-effector position/orientation, utilizing transformation matrices and kinematic diagrams, the paper provides a solid framework for predicting manipulator behavior across different configurations.
<br>

<p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Furthermore, this paper explores into the inverse kinematics problem, concentrating on identifying the joint variables required to reach a desired end-effector position. This investigation is complemented by an examination of how manipulator design parameters, such as link lengths and joint limitations, affect both forward and inverse kinematics solutions. By highlighting the significance of these factors in manipulator design and optimization, the study emphasizes the need to consider them comprehensively for achieving optimal performance.
<br>

<p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Understanding the joint variables essential for achieving specific end-effector positions is crucial for effective manipulator operation. Additionally, recognizing how design parameters impact kinematics solutions provides valuable insights into enhancing manipulator efficiency and functionality. Therefore, this research contributes to advancing the field by emphasizing the importance of considering both inverse kinematics and design parameters in the development and optimization of cylindrical manipulators.
<br>

<p align="justify"> 
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Through programming, computational analyses and experimental validations, the accuracy and feasibility of the derived kinematic models are thoroughly assessed under various operating conditions and environments. The insights gained from this study are invaluable for the design, control, and optimization of cylindrical manipulators and hold promise for enhancing efficiency, productivity, and versatility in robotics and automation across diverse industries. Overall, the computation of forward and inverse kinematics is poised to make significant contributions to the advancement of robotics and automation, driving innovation and progress in the field.
  
</p>
<br>



## II. Introduction

<p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The robot manipulators nowadays play a vital role in the manufacturing industries. Jobs that require high precision and repeatability such as packaging, labelling and assembling of products are carried out by robots. (Prasad et al., 2017). Cylindrical manipulators are known for their cylindrical shape and flexible joints, making them adept at precise tasks across various industries. With interconnected links and joints arranged cylindrically, these robots possess a unique blend of mobility and agility, enabling them to navigate tight spaces and execute intricate maneuvers accurately.
</p>

<p align="justify">
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Moreover, Degrees of freedom (DOF) are crucial for understanding the motion capabilities of cylindrical manipulators, which are widely utilized in industrial automation and robotics. DOF represent the number of independent movements a manipulator can perform, essential for assessing its flexibility and range of motion. In cylindrical manipulators, DOF are determined by the configuration and arrangement of their joints, typically comprising prismatic and revolute joints. Understanding the degrees of freedom of cylindrical manipulators is essential for ensuring their effective performance in various applications.
</p>

<p align="justify">
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Kinematic diagrams and Denavit-Hartenberg (DH) frame assignment are essential tools for understanding the motion characteristics of cylindrical manipulators, which play a significant role in industrial automation and robotics. Kinematic diagrams provide a visual representation of the mechanical structure and motion of a manipulator, illustrating the relationships between its links, joints, and end-effector. By utilizing kinematic diagrams, engineers can analyze the kinematics of cylindrical manipulators and optimize their design for specific tasks and environments.
</p>

<p align="justify">
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Similarly, DH frame assignment is a standardized method for representing the kinematic structure of manipulators, assigning frames to each link and defining parameters such as joint angles and link lengths. This approach simplifies the derivation of kinematic equations and the calculation of transformation matrices, enabling efficient analysis and control of cylindrical manipulators. Understanding kinematic diagrams and DH frame assignment is 
essential for effectively analyzing and controlling the motion of cylindrical manipulators, enabling researchers to gain insights into the manipulator's kinematic behavior and optimize its performance for various industrial applications.
</p>

<p align="justify">
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Forward kinematics (FK) defines the position and orientation of the end-effector as a function of the joint angles coordinates. It is an easy task that is generally solved using Denavit–Hartenberg (D–H) matrix parameter table (Iliukhin et al., 2017). The Denavit-Hartenberg (DH) parametric table serves as a foundation tool for characterizing the kinematic structure of cylindrical manipulators, which are integral components of industrial automation and robotics. The DH parametric table systematically organizes the geometric parameters and transformation matrices associated with each link and joint of the manipulator, providing a concise representation of its kinematic properties. By utilizing the DH parametric table, engineers can derive kinematic equations and compute forward and inverse kinematics solutions for cylindrical manipulators with ease and efficiency. This facilitates the analysis, design, and control of manipulator systems, enabling precise and reliable operation in diverse industrial settings. Understanding the DH parametric table is essential for effectively modeling and analyzing the kinematics of cylindrical manipulators, simplifying the kinematic analysis process and enhancing the overall efficiency of manipulator design and control.
</p>

<p align="justify">
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Homogeneous transformation matrices are fundamental mathematical tools essential for understanding the spatial relationships and transformations within cylindrical manipulators, pivotal components of industrial automation and robotics. According to Maram et al. (2019), Homogeneous Transformation Matrix (HTM) comprises a rotation matrix representing orientation and a position vector representing position. HTMs are extensively utilized in forward and inverse kinematic formulations of robots. By leveraging homogeneous transformation matrices, engineers can precisely model the movement and positioning of cylindrical manipulators, facilitating efficient trajectory planning, motion control, and task execution across diverse industrial applications.
</p>

<p align="justify">
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The development of graphical user interface (GUI) calculators for both forward and inverse kinematics represents a significant advancement in the field of cylindrical manipulators, crucial for simplifying design and analysis processes. These intuitive tools provide engineers and researchers with user-friendly interfaces to input manipulator parameters and compute kinematic solutions efficiently. By incorporating GUI calculators into the design work flow, users can quickly assess the motion capabilities of cylindrical manipulators and optimize their performance for specific tasks and environments. This integration of technology holds promise for streamlining the design, control, and optimization of manipulator systems, fostering advancements in industrial automation and robotics with enhanced accessibility and usability
</p>
<br>


## III. Degrees of Freedom

  <p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Degrees of Freedom (DOF) in robotics refer to the number of independent parameters or axes along which a robot can move. Each degree of freedom corresponds to a specific joint or axis within the robotic system, allowing motion in a particular direction. For example, a robotic arm with multiple joints may have several degrees of freedom, enabling it to perform complex movements. Understanding the degrees of freedom is crucial for robot designers and engineers to determine the robot's capabilities and limitations in various tasks. It influences the robot's ability to navigate its environment, manipulate objects, and interact with its surroundings. By optimizing the degrees of freedom, robotic systems can achieve greater flexibility and effectiveness in accomplishing their intended functions.</p>
  
<p class="blank-line">&nbsp;</p>

**IDEAL DOF**
  - A **point** in 2D: 2-DOF; in 3D space: 3-DOF
  - A **rigid body** in 3D: 6-DOF
  - **Planar Manipulator**: 3-DOF
  - **Spatial manipulator**: 6-DOF
<br>

#### Based on the number of degrees of freedom, mechanical manipulator can be categorized into several types:
<div align="justify">
    
 1. ***Under Actuated Manipulator***
      + Planar Manipulator_ with less than 3-DOF
      + Spatial Manipulator_ with less than 6-DOF
</p>
  
 2. ***Ideal Manipulator***
      + Planar Manipulator_ with exactly 3-DOF
      + Spatial Manipulator_ with exactly 6-DOF
</p>
  
 3. ***Redundant Manipulator***
      + Planar Manipulator_ with more than 3-DOF
      + Spatial Manipulator_ with more than 6-DOF
</p> 
<br>


#### Grubler's Criterion for Mobility
<div align="justify">
  
1.**Formula for the Mobility of _Spatial Manipulator**
    $$M = 6n - \sum_{i=1}^m (6-Ci)$$
</p>    
   
2.**Formula for the Mobility of _Planar Manipulator**
    $$M = 3n - \sum_{i=1}^m (3-Ci)$$    
</p>  

where in:
</p> 
    n = is the total number of links or bodies in the mechanism.</p> 
    Ci= represent the connectivity of joint.</p> 
    
</div>

<br>

### Computation of Deegrees of Freedom (DOF) of Cylindrical Manipulator:
___

<div align="center">
    
<img src="![DOF-Cylindircal Manipulator](https://github.com/yoboiqk/Robotics2_FK-IK_Group-1_Cylindrical-manipulator_2024/assets/157770806/17527171-773f-4a5a-8b9f-866b7bf37dd4)" width="400" height="250">
</p> 

 ***Figure 1. DOF of RPP***
 
</div>
<br>


  <p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The Figure 1 represents a Cylindrical Manipulator (RPP) featuring one revolute joint and two prismatic joints, commonly utilized in robotics for various applications. The Degrees of Freedom of this manipulator are calculated using Grubler’s Criterion for Mobility, which is applicable to spatial manipulators like the cylindrical manipulator. Based on the computation, it is determined that the cylindrical manipulator possesses three degrees of freedom. Consequently, it is classified as an Under-Actuated Spatial Manipulator, indicating its capacity for movement within a three-dimensional space. 
</p>
<br>

#### Degrees of Freedom of a Cylindrical Manipulator Tutorial Video


<br>



## IV. Kinematic Diagram and D-H Frame
  <p align="center">
  <img src="![Screenshot 2024-04-04 215403](https://github.com/yoboiqk/Robotics2_FK-IK_Group-1_Cylindrical-manipulator_2024/assets/157770806/9b846719-2d8b-4162-8ad6-93f2452a821d)" width="250" height="500">
     </p> 

 ***Figure 2. Kinematic Diagram of RPP***
</p> 
</div>
<br>

  <p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A Kinematic Diagram in robotics is a representation used to illustrate the motion and geometry of a mechanical manipulator. It describe the arrangement of links and joints of the mechanical manipulator. The diagram shows the connections between these components, such as revolute and prismatic joints, which enable movement.     
</p>

**MECHANICAL MANIPULATOR ANATOMY**

1.**_BASE_**- it support mechanical manipulator.</p>
2.**_LINK_**- a rigid member that connects the joints.It can be input link and output link.</p>
3.**_JOINT_**- it integrates 2 or more links to provide controlled relative movement by input and output link.
4.**_END EFFECTOR_**- it is any device at the end of mechanical manipulator which is shaped like a hand or a special tool depending upon the application.
</p>
<br>

### D-H Frame Assignment
___

 <p align="justify"> 
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>Jacques Denavit</b> and <b>Richard</b> Hartenberg introduced the Denavit-Hartenberg (DH) convention in 1955 to standardize the coordinate frames for spatial linkages. The DH notation is utilized to solve forward kinematics for mechanical manipulators. DH Frame Rules are employed to assign frames in a kinematic diagram for applying the DH notation.</p>
     
In mechanical manipulator a coordinate system that the manipulator knows where it is or where to go. There are 3 types of frame used on mechanical manipulator  and these are the following: </p>
* BASE  (WORLD) FRAME 
* USER FRAME
* TOOL FRAME 

</p>


<br>

When assigning frames, certain rules must be followed and these is the D-H Frame Rule.
+ **_Rule 1_**: The z axis must be the axis of rotation for a revolute/twisting joint, or the direction of translation for a prismatic joint.
+ **_Rule 2_**: The x axis must be perpendicular both to its own Z axis, and the Z axis of the frame before it.
+ **_Rule 3_**: Each axis must intersect the z axis of the frame before it. The rules for complying rule 3: </p>
   + Rotate the axis until it hits the other.</p>
    + Translate the axis until it hits the other.</p>
+ **_Rule 4_**: All frames must follow the right hand rule. 
<br>


### Kinematic Diagram and D-H Frame Assignment of Cylindrical Manipulator
___

<p align="center">
  <img src="![433076609_1081756836384490_8332537221389561292_n](https://github.com/yoboiqk/Robotics2_FK-IK_Group-1_Cylindrical-manipulator_2024/assets/157770806/22e66f74-2351-4a77-b630-e40ac23f21bc)"
width="350" height="500"></p>

 ***Figure 3. Kinematic Diagram and D-H Frame of RPP***

</div>
<br>

<p align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


</p>
<br>


#### Kinematic Diagram and D-H Frame of a Cylindrical Manipulator Tutorial Video



<br>






















# Robotics2_FK-IK_Group-1_Cylindrical-manipulator_2024
This is our laboratory 1 : FORWARD and INVERSE KINEMATICS

A. Kinematic Diagram with labels and frames.
![429066715_3530844397176694_452290936478799161_n](https://github.com/yoboiqk/Robotics2_FK-IK_Group-1_Cylindrical-manipulator_2024/assets/157770806/0457f136-8c4f-4372-9079-0e989f3aa622)

B. Parametric Table
![429858259_796626322506425_7379598378023722392_n](https://github.com/yoboiqk/Robotics2_FK-IK_Group-1_Cylindrical-manipulator_2024/assets/157770806/964b3869-3546-450a-a6dd-e4194e88df72)

C. MATLAB and Python codes
    
    The MATLAB code is attached in the MATLAB code Folder and  The Python codes is attached in the Python codes Folder.

D. Tables for the comparison of Forward Kinematics and Inverse Kinematics in MATLAB and Python 
    
    The tables for the comparison of Forward Kinematics and Inverse Kinematics in MATLAB and Python are attached in the 2 folders for Forward Kinematics and Inverse Kinematics.
