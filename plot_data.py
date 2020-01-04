import pickle
import matplotlib.pyplot as plt

python_data=pickle.load(open('./python_add_time.data', 'rb'))
numpy_data=pickle.load(open('./numpy_add_time.data', 'rb'))
python_nb_data=pickle.load(open('./python_nb_add_time.data', 'rb'))

input_value=[]

i=10
while i<=1000:
    input_value.append(i)
    i+=10

list_py_data=[]
list_num_data=[]
list_py_nb_data=[]

for a in python_data:
    list_py_data.append(python_data[a])

for b in numpy_data:
    list_num_data.append(numpy_data[a])

for b in python_nb_data:
    list_py_nb_data.append(python_nb_data[a])
    

plt.xlabel("N value")
plt.ylabel("Time (seconds(s))")
plt.plot(input_value, list_py_data)
plt.plot(input_value, list_num_data)
plt.plot(input_value, list_py_nb_data)
plt.show()
