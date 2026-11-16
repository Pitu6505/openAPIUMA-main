from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
from qiskit.providers.basic_provider import BasicProvider
from qiskit_ibm_provider import IBMProvider

qreg_q = QuantumRegister(3, 'q')
creg_c = ClassicalRegister(3, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.h(qreg_q[0])
circuit.h(qreg_q[1])
circuit.h(qreg_q[0])
circuit.x(qreg_q[0])
circuit.z(qreg_q[2])
circuit.measure(qreg_q[0], creg_c[0])
circuit.measure(qreg_q[1], creg_c[1])
circuit.measure(qreg_q[2], creg_c[2])

gate_machines_arn = {
    "local": "local",
    "ibm_brisbane": "ibm_brisbane",
    "ibm_osaka": "ibm_osaka",
    "ibm_kyoto": "ibm_kyoto",
    "simulator_stabilizer": "simulator_stabilizer",
    "simulator_mps": "simulator_mps",
    "simulator_extended_stabilizer": "simulator_extended_stabilizer",
    "simulator_statevector": "simulator_statevector",
}
if machine == "local":
    backend = BasicProvider().get_backend("basic_simulator")
else:
    provider = IBMProvider()
    backend = provider.get_backend(gate_machines_arn[machine])
transpiled_circuit = transpile(circuit, backend)
job = backend.run(transpiled_circuit, shots=int(shots))
result = job.result()
return result.get_counts()
