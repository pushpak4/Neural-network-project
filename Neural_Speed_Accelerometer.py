import numpy as np
import csv, time

speed=[]  #List to store the entire speed data from the CSV file
accX=[]   #List to store the entire accX  data from the CSV file
counter=0
t_counter=1

with open('dataa.csv','r') as csv_file:
        data=csv.reader(csv_file,delimiter=',')
        for row in data:
            speeds=row[1]
            accler=row[2]
            speed.append(speeds)
            accX.append(accler)

alphas = [10]

# compute sigmoid nonlinearity
def sigmoid(x):
        output = 1 / (1 + np.exp(-x))
        return output

# convert output of sigmoid function to its derivative
def sigmoid_output_to_derivative(output):
    return output * (1 - output)

while(1):
    X = np.array([[0, 1, 1],
                  [1, 0, 1],
                  [0, 0, 1],
                  [1, 1, 1]])
    y = np.array([[1],
              [1],
              [0],
              [1]])
    if (float(speed[counter]) >308.32):
         X[0,0]=1
         if (int(accX[counter])>0):
             X[0,1]=1
         else:
             X[0,1]=0
    else:
        X[0,0]=0
    counter+=1

    if (float(speed[counter]) >308.67):
         X[1,0]=1
         if(int(accX[counter])>0):
             X[1,1]=1
         else:
             X[1,1]=0
    else:
        X[1,0]=0
    counter+=1

    if (float(speed[counter]) >308.89):
        X[2,0]=1
        if (int(accX[counter])>0):
            X[2,1]=1
        else:
            X[2,1]=0
    else:
        X[2,0]=0
    counter+=1
    
    if (float(speed[counter])>308.45):
        X[3,0]=1
        if (int(accX[counter])>0):
            X[3,1]=1
        else:
            X[3,1]=0
    else:
        X[3,0]=0
        
    counter+=1
    print(X[0,0],X[1,0],X[2,0],X[3,0])
    print(X[0,1],X[1,1],X[2,1],X[3,1])

    for alpha in alphas:
        print ("\n\nARTIFICIAL NEURAL NETWORK\nBinary Input and Output ANN with One Hidden Layer\n")
        print ("\nTraining With Alpha:" + str(alpha))
        np.random.seed(1)
        # randomly initialize our weights with mean 0
        synapse_0 = np.random.random((3, 4))
        synapse_1 = np.random.random((4, 1))

        prev_synapse_0_weight_update=np.zeros_like(synapse_0)
        prev_synapse_1_weight_update=np.zeros_like(synapse_1)
        synapse_0_direction_count=np.zeros_like(synapse_0)
        synapse_1_direction_count=np.zeros_like(synapse_1)

    for j in range (60000):
          #Feed forward through layers 0, 1, and 2
          layer_0 = X
          layer_1 = sigmoid(np.dot(layer_0, synapse_0))
          layer_2 = sigmoid(np.dot(layer_1, synapse_1))
          # how much did we miss the target value?
          layer_2_error =  y - layer_2

          if (j % 10000) == 0:
              print ("Error after " + str(j) + " iterations:" + str(np.mean(np.abs(layer_2_error))))
              # in what direction is the target value?

              # were we really sure? if so, don't change too much.
          layer_2_delta = layer_2_error * sigmoid_output_to_derivative(layer_2)

          # how much did each l1 value contribute to the l2 error (according to the weights)?

          layer_1_error = layer_2_delta.dot(synapse_1.T)


          # in what direction is the target l1?

          # were we really sure? if so, don't change too much.
          layer_1_delta = layer_1_error * sigmoid_output_to_derivative(layer_1)
          synapse_1_weight_update = (layer_1.T.dot(layer_2_delta))
          synapse_0_weight_update =  (layer_0.T.dot(layer_1_delta))

          if (j > 0):
              synapse_0_direction_count += np.abs(((synapse_0_weight_update > 0) + 0) - ((prev_synapse_0_weight_update > 0) + 0))
              synapse_1_direction_count += np.abs(((synapse_1_weight_update > 0) + 0) - ((prev_synapse_1_weight_update > 0) + 0))

          synapse_1 += alpha * synapse_1_weight_update
          synapse_0 += alpha * synapse_0_weight_update

          prev_synapse_0_weight_update = synapse_0_weight_update
          prev_synapse_1_weight_update = synapse_1_weight_update

    print ("Synapse 0")
    print (synapse_0)
    print("Synapse 0 Update Direction Changes")
    print (synapse_0_direction_count)
    print ("Synapse 1")
    print (synapse_1)
    print ("Synapse 1 Update Direction Changes")
    print (synapse_1_direction_count)

    #Feed forward through layers 0, 1, and 2
    layer_0 = [0, 0, 0]
    layer_1 = sigmoid(np.dot(layer_0, synapse_0))
    layer_2 = sigmoid(np.dot(layer_1, synapse_1))
    print(layer_2)
    print("\nFor Input [0, 0, 0] the Output is")
    if layer_2 > 0.75:
        print ('The speed got exceeded please reduce the speed')
    if layer_2 < 0.75:
        print ('speed is ok')
    print(t_counter)
    t_counter+=1
    time.sleep(2.0)




