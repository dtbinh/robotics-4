import memory, commands
import core
import mem_objects
from task import Task
from state_machine import *

class Playing(Task):
  def run(self):
    ball = memory.world_objects.getObjPtr(core.WO_BALL)
    print "aaaaaaaaa"
    if ball.seen:
      #print "ball.visionBearing is %f!" % ball.visionBearing
      print "I have seen the blue goal"
      commands.setStiffness()
      if ball.visionBearing > 0.20:
        commands.setWalkVelocity(0, 0, 0.3)
      elif ball.visionBearing < -0.20:
        commands.setWalkVelocity(0, 0, -0.3)
      else:
        print "ball.visionDistance is %f!" % ball.visionDistance  
        if ball.visionDistance > 2200:
          commands.setWalkVelocity(0.6, 0, 0)
        elif ball.visionDistance < 1500:
          commands.setWalkVelocity(0, 0, 0)
        else:
          commands.setWalkVelocity(0, 0, 0)
    else:
      print "I don't see anything"
	
