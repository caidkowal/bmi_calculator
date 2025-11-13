import math
import matplotlib.pyplot as plt
import numpy as np
class Bodymassindex:
  """
  A class used to model the New BMI and Old BMI graphs

  ...

  Methods
  -------
  open()
    opens a file and creates a list of each attribute in every human. Creates a list of BMI values for every human. Creates a model for Age vs Bmi graph and Weight vs New Bmi Graph
    
  create_bmi_list()
  creates a BMI list and appends the BMI values to the list, returns BMI list
  
  BMIcalculator()
  calculates and returns BMI value

  newBMIcalculator()
  calculates and returns New BMi value 

  regression_calculation()
  calculates and returns the slope, intercept, and correlation coefficent for each model.

  graph()
  graphs the model( either Age vs Bmi or Weight vs New BMI)
  """
  
  def open(self, filename):
    """
    opens a file and creates a list of each attribute     in every human. Creates a list of BMI values for       every human. Creates a model for Age vs Bmi graph and   Weight vs New Bmi Graph

  
  Args:
    filename: the name of the file that it should open
    
  """
    file = open(filename, "r")

    lines = file.readlines()

    humans_list = []

    for data in lines:
      line = data.split()

      humans_list.append(line)

    age_list = []
    weight_list = []
    height_list = []
    chestdiameter_list = []
    chestdepth_list = []
    bitrochantericdiameter_list = []
    wristgirth_list = []
    anklegirth_list = []
    new_bmi_list = []
    old_bmi_list = []

    # The number of lines/humans
    N = len(age_list)
    
    # takes in attributes for each human and adds them to list
    for attribute in humans_list:
      age_list.append(float(str(attribute[21])))

      weight_list.append(float(str(attribute[22])))

      height_list.append(float(str(attribute[23]))/100)

      chestdiameter_list.append(float(str(attribute[3]))) 

      chestdepth_list.append(float(str(attribute[2])))

      bitrochantericdiameter_list.append(float(str(attribute[1])))

      wristgirth_list.append(float(str(attribute[20])))

      anklegirth_list.append(float(str(attribute[19])))
    
      

      # Create list of new BMI values
      new_bmi_list.append( self.newBMIcalculator(  \
                      chestdiameter_list[-1], \
                      chestdepth_list[-1], \
                      bitrochantericdiameter_list[-1], \
                      wristgirth_list[-1],  \
                      anklegirth_list[-1], \
                      height_list[-1]))


    # Get list of bmi values
    BMI_list = self.create_bmi_list(weight_list, height_list)
      
    #Age = X, BMI = Y
    self.Age_vs_BMI = [age_list, BMI_list]


    #Weight = X, newBMI= Y
    self.Weight_vs_newBMI = [weight_list, new_bmi_list]
    
    
    
  
  def create_bmi_list(self, w_list, h_list):
    """
    creates a BMI list and adds the BMI values of every     human to the list
  Args:
  w_list: the first list that it uses to create BMI values (weight list)
  h_list: the second list that it uses to create BMI values (height list)
  Returns:
    a list with BMI values of every human

  """
    b_list = []
    
    for index in range(len(w_list)):
      b_list.append(self.BMIcalculator(w_list[index], h_list[index]))

    return b_list
  
  def BMIcalculator(self,weight, height):
    """
    calculates the bmi value
  Args:
    weight: the weight of a human
    height: the height of a human
  Returns:
    the bmi value

  """
    
    BMI = weight/height**2
    return BMI
    


  
  def newBMIcalculator(self,chestdiameter, chestdepth, bitrochantericdiameter, wristgirth, anklegirth, height):
    """
    calculates the New BMI value
  Args:
    chestdiameter: the chest diameter of a human
    chestdepth: the chest depth of a human
    bitrochantericdiameter: the bitrochanteric diameter of a human
    wristgirth: the wrist girth of a human
    anklegirth: the ankle girth of a human
    height: the height of a human
    
    
  Returns:
    the New BMI value

  """


    newBMI =  -110 + chestdiameter*1.34 + chestdepth*1.54 + bitrochantericdiameter*1.20 + wristgirth*1.11 + anklegirth*1.15 + height*0.177
    
    return newBMI

  
  
  def regression_calculation(self,model):
    """
    calculates the slope, intercept, and correlation coefficent of the line for each model
  Args:
    model: the X,Y pair of values it uses
  Returns:
    the slope, intercept, and correlation coeffecient of the the line for the model

  """
  
    xlist = model[0]
    ylist = model[1]
    N =  len(model[0])
    
    sumX = sum(xlist)
    sumY = sum(ylist)
  
    sumXY = 0
    sumXSquared = 0
    sumYSquared = 0


    
    for index in range(N):
      
      sumXY += xlist[index] * ylist[index]
  
      sumXSquared += xlist[index]**2
      
      sumYSquared += ylist[index]**2

  
    slope = (N*sumXY - (sumX*sumY))/(N*sumXSquared - (sumX)**2)
  
    intercept = (sumY - (slope*sumX))/N
  
    corr = (N*sumXY - (sumX*sumY)) / math.sqrt((N*sumXSquared - (sumX)**2) * (N*sumYSquared - (sumY)**2))
  
  
    return (slope, intercept, corr)

  
  def graph(self, type ):
    """
    graphs a model
  Args:
    type: the type of model that the function should graph(old_bmi or new_bmi)

  """

    lin = np.linspace(0,150,150)

    if type == "old_bmi":
      line = (self.regression_calculation(self.Age_vs_BMI)[0] * lin)+ self.regression_calculation(self.Age_vs_BMI)[1]
      plt.title('BMI vs Age')
      plt.xlabel('Ages')
      plt.ylabel('BMIs')

    xlist = self.Age_vs_BMI[0]
    ylist = self.Age_vs_BMI[1]
    
    if type== "new_bmi":
      line = (self.regression_calculation(self.Weight_vs_newBMI)[0] * lin) + self.regression_calculation(self.Weight_vs_newBMI)[1]
      plt.title('Weight vs New BMI')
      plt.xlabel('Weight')
      plt.ylabel('New BMIs')

      xlist = self.Weight_vs_newBMI[0]
      ylist = self.Weight_vs_newBMI[1]
      
    plt.plot(line, '--r')
    plt.scatter(xlist,ylist)
    plt.show()
  

b = Bodymassindex()
b.open('body.dat')
b.graph("new_bmi")