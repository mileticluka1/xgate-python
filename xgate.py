# First, we import the necessary modules
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer

# Next, we create a quantum circuit with a single qubit and a classical register
q = QuantumRegister(1)
c = ClassicalRegister(1)
circuit = QuantumCircuit(q, c)

# Now, we apply the Xgate to the qubit
circuit.x(q[0])

# Finally, we measure the qubit and store the result in the classical register
circuit.measure(q, c)

# Now, we can execute the circuit and see the result
backend = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend, shots=1).result()
print(result.get_counts())
