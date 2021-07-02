# **Turtlesim_CatchAndCatch**


This is a fun implementation of Catch and Catch game done using ROS Turtlesim.

The game is basically, there a initial turtle which is the catcher of the game . A new turtle is spawing to which the catcher is going to the goal position to catch the new turtle. Everytime we catch a turtle a new turtle is spawing in a random position. This process repeats continuously
<p>
<h3><b>Flow of program</b></h3>
  <br><ul><li>locating random positions</li><br>
  <li>spawning new turtle</li><br>
  <li>identifing distance</li><br>
  <li>equating the distance</li><br>
  <li>killing turtle</li> <br></ul></p>
  
<ul>
  <p>
  <li><h5>Locating random positions<h5></li>
    > random.randrange() <br>
    This function can output a random value between the range of value we give it as a input. So by using this we can locate and spawn in random different positions of the turtlesim workspace.</p>
    <p>
    <li><h5>Spawning new turtle</h5></li>
    >Turtle_spawn(goal,killer_name,spawn_name)<br>
    By using this function we can create a new turtle anywhere in the screen according to our inputs. The inputs are <br>
    goal = position<br>
    killer_name and spawn_name <br>
    So the turtle will be spawn at the goal position with the name of spawn_name
    </p>
    <p>
    <li><h5>Identifying Distance</h5></li>
      The distance between the spawn turtle and the Catcher turtle is found using the function <br>
      >euclidean_distance(self, goal_pose)
    </p>
    <p>
      <li><h5>Equating the distance</h5></li>
      Equating the distance between the turtles with the tolerance level , the linear and angular velocities of the turtle is changed simultaneously<br>
      >while self.euclidean_distance(goal_pose) >= float(distance_tolerance):<br>
      With that the turtle moves towards the catching the new turtles
    </p>
     
    
    <p>
      <li><h5>Killing turtle</h5></li>
      >Turtle_kill(killer_name)<br>
      This function is used to kill the turtle whose input parameter is the name of the turtle. Once the Catcher turtle catches the newly spawned turtle. Then the Turtle_Kill function is been called<br>
      >self.Turtle_kill('turtle2')
    </p>

  </ul>

![Screenshot from 2021-06-30 14-39-58(1)](https://user-images.githubusercontent.com/58605350/124026120-e87f8280-da0e-11eb-89d0-d316f0e9f482.png)


You can also view the result [here](https://www.youtube.com/watch?v=MuM3U3kca-8).
