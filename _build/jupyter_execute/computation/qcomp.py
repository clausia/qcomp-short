#!/usr/bin/env python
# coding: utf-8

# (sec-qcomp)=
# # Quantum computation
# 
# The construction of current quantum computers is based on the so-called [*quantum circuit model*](https://en.wikipedia.org/wiki/Quantum_circuit). It requires the following five components.
# 
# 1. Many qubits.
# 2. The ability to reset the qubits.
# 3. A set of quantum operations (called quantum gates) that can entangle the qubits.
# 4. A classical computer that applies a circuit of quantum gates on the qubits.
# 5. The ability to measure the qubits in the computational basis and read out the classical bits.
# 
# It is necessary for you to understand the structure of the quantum computers at this stage.  The very purpose of this book is to learn them. The followings are the brief summary of the construction. If you are interested in the details of the above requirements, see Ref. {cite}`DiVincenzo2000`.  

# ## Qubits
# 
# Quantum computers are also made of many small building blocks but unlike classical computers we need to use quantum mechanics to describe their state. Current quantum computers use the smallest quantum system, that is a two-dimensional Hilbert space $\mathbb{C}_2$ spanned by complex vectors $\lvert 0 \rangle$ and $\lvert 1 \rangle$, known as _qubit_. These two basis states looks similar to `0` and `1` for a classical bit . However, unlike the classical bit,  the state of a qubit  can be in a superposition state
# 
# $$
# |\psi\rangle = c_{0} \lvert 0 \rangle + c_{1} \lvert 1 \rangle
# $$ (eqn:superposition)
# 
# where $c_0$ and $c_1$ are complex number satisfying $|c_0|^2+|c_1|^2=1$ (normalization). Similarly to the classical bit, we obtain either $|0\rangle$ or $\lvert 1 \rangle$  when the superposition state is measured.   We shall call them _computational basis_. However,  the state of the qubit is neither $\lvert 0 \rangle$ nor $\lvert 1 \rangle$  but  $\lvert 0 \rangle$ AND $\lvert 1 \rangle$ simultaneously. Hence, a qubit can compute two different cases at once (if a programmer is smart enough). Quantum computers exploit this superposition state.  Unlike the classical bit which has only two possible states, a qubit can take infinitely many different states since $c_0$ and $c_1$ can be any complex numbers satisfying the normalization condition. 
# 
# Obviously, quantum computers are made of many qubits as a composite system. Let us consider two qubits, $q_0$ and $q_1$.  A composite system of two classical bits can have four different states, '00', '01', 10', and '11'.  Similarly  the pair of qubits are spanned by four basis vectors $\lvert 00 \rangle$, $\lvert 01 \rangle$, $\lvert 10 \rangle$, and $\lvert 11 \rangle$.  Unlike the classical bits, the qubits can be in a superposition state
#  
# $$
# \lvert \psi \rangle = c_{00} \lvert 00 \rangle + c_{01} \lvert 01 \rangle + c_{10} \lvert 10 \rangle + c_{00} \lvert 11 \rangle
# $$
# 
# The four different possibilities are simultaneously considered in the superposition state. The complexity of the superposition state grows very rapidly as the number of qubits increases.  If there are $n$ qubits, the number of terms in the superposition state can be as many as $2^n$.   Then, $2^n$ different cases are simultaneously computed. We will take the advantage in various applications.
# 
# In classical computers,  a bit string $b_{n-1}\, b_{n-2}\,\cdots\, b_1\, b_0$ expresses the state of the system.  In quantum computer, a tensor product $\lvert q_{n-1} \rangle \otimes \lvert q_{n-2}\rangle \otimes \cdots \otimes \lvert q_1 \rangle \otimes \lvert q_0 \rangle$ represents the state of $n$ qubits.  For two qubits, $\lvert 01 \rangle = \lvert 0 \rangle \otimes \lvert 1 \rangle$.

# ## Resetting a qubit
# 
# Suppose that a qubit is in an arbitrary state $|\psi\rangle$.  We want to transform the state to $|0\rangle$ or the lowest energy state.  This process is known as *resetting*.  The resetting is by no means trivial.  Actually, it is very difficult due to the restrictions listed in {numref}`sec-qinfo` and other restrictions set by the laws of thermodynamics.  The resetting on current quantum computers is not perfect.
# 

# ## Circuit models
# 
# The time-evolution of qubits  is a unitary transformation determined by the Shcr&ouml;dinger equation.  Quantum computers manipulate the qubits by applying a unitary operator $U$.  Starting an initial state $|\psi_i\rangle$, the final state (the solution of the quantum computation) is mathematically given by $|\psi_f\rangle = U |\psi_i\rangle$.  The quantum algorithm determines the unitary operator $U$. Recall that $U$ is $2^n \times 2^n$ matrix for $n$ qubits, which is huge.   How can we construct such a huge matrix?  It turns out that a set of signle qubit unitary operators ($2\times 2$ matrix) and two-qubit unitary operators ($4 \times 4$) can realize $U$.  Such unitary matrices are knwon as *gates*.  To obtain a desired final state, we just apply a set of one-qubit gates and two-qubit gates successively.  In addition to the unitaries, we also need to measure the qubits using measurement gates.  The set of the gates is called [*quantum circuit*](https://en.wikipedia.org/wiki/Quantum_circuit).  A simple example is given below.

# ## Gates
# 
# As a general purpose computer, a quantum computer must be able to change the state of qubits based on given instructions. Recall that a classical bit can only be flipped.  In contrast, quantum computers can change the state of a qubit in infinitely many different ways.  Here we use also the concept of gates.  A qubit enters a gate and comes out in a different state.  In other words, a state vector of the qubit is transformed to another state vector by the gate.  In quantum mechanics, that is achieved by a unitary transformation $U$.   The transformation $|\psi'\rangle=U |\psi\rangle$ in quantum mechanics is equivalent to applying a 1-qubit gate $U$ to a qubit and expressed as
# 
# ```{figure} u1-gate.png
# ---
# name: u1-gate
# ---
# Action of one-qubit gate.
# ```
# 
# As an example, consider a Pauli operator $X \equiv \sigma_x$.  When it acts on the computational basis, $X \lvert 0 \rangle = \lvert 1 \rangle$ and $X \lvert 1 \rangle=\lvert 0 \rangle$.  Hence, it acts like $\texttt{NOT}$ in the classical computation. See the {numref}`quantum-gate-X`. The qubit can be in a superposition state.  The  classical truth table is not enough. When it acts on a general state, we get
# 
# $$
# X \lvert \psi \rangle = c_0 X \lvert 0 \rangle + c_1 X \lvert 1 \rangle = c_0 \lvert 1 \rangle + c_1 \lvert 0 \rangle = c_1 \lvert 0 \rangle + c_0 \lvert 1 \rangle
# $$ (Xgate)
# 
# which actually swaps the coefficients.  The first two rows in  {numref}`quantum-gate-X` is much like the classical truth {numref}`table %s <classical-NOT>`.  The third row makes quantum computers more powerful than the classical computers.
# 
# 

# ```{table} X Gate
# :name: quantum-gate-X
# | &nbsp;| $i$ | $o$ |
# | :---:| :---: | :---: |
# | &nbsp;| $\lvert 0 \rangle$ | $\lvert 1 \rangle$  |
# | &nbsp;| $\lvert 1 \rangle$ | $\lvert 0 \rangle$  |
# | &nbsp;| $c_0 \lvert 0 \rangle + c_1 \lvert 1 \rangle$ | $c_1 \lvert 0 \rangle + c_0 \lvert 1 \rangle$ |
# ```

# Like classical computers, quantum computers use gates that take two qubits as input.   Two-qubit gates are also a unitary operator and express as
# 
# ```{figure} u2-gate.png
# ---
# name: u2-gate
# ---
# Action of two-qubit gate.
# ```
# 
# 
# Logically, infinitely many 1-qubit and 2-qubits gates are possible but it is known that only several basic gates such as X, Z, and CX are actually needed to carry out quantum computation. Depending on the underlying quantum systems, the available gates are different.  However, almost any gate can be expressed equivalently with a set of other gates in principle (gate _decomposition_).  So, if a desired gate is not available on the device you are using, you  must find an alternative gate. 

# ## Encoding
# 
# Encoding the information of the problem to be solved to qubits in a quantum computer is not a trivial task.  Let us try to use the same encoding scheme as the above classical case: 
# 
# $$
# \texttt{False} \Rightarrow \lvert 0 \rangle, \quad \texttt{True} \Rightarrow \lvert 1 \rangle
# $$
# 
# This works fine.  However, there are many other encoding schemes since a qubit can take a superposition state.  For example,
# 
# $$
# \texttt{False} \Rightarrow \lvert + \rangle \equiv \frac{1}{\sqrt{2}}\left(\lvert 0 \rangle+\lvert 1 \rangle\right), \quad
# \texttt{True}  \Rightarrow \lvert - \rangle \equiv \frac{1}{\sqrt{2}}\left(\lvert 0 \rangle-\lvert 1 \rangle\right)
# $$
# 
# is another choice. 
# 
# To make a good use of quantum computer, finding a good encoding scheme is crucial.
# 

# ## Circuits
# 
# Once an encoding scheme is chosen, we need to give a set of instructions to a quantum computer.  That is we find a set of unitary operators that are applied on qubits one after the other. Unlike classical computation, no advanced programming language is available for quantum computing.  Therefore, programmers must right  instructions the device can understand directly (similar to coding with machine or assembly language for classical computers.)  A code for quantum computation looks like
# 
# 
# ```{figure} qc.png
# ---
# name: qc-example
# ---
# An example of quantum circuit.
# ```
# 
# which is known as quantum circuit.  Each object in the circuit is a unitary gate.
# 
# The following circuit computes $x \oplus y$ using a quantum computer.
# 
# 
# ```{figure} quantum_x+y.png
# ---
# name: quantum_x+y
# ---
# Quantum computation of $x \oplus y$.
# ```
# 
# The gate in the circuit is known as _controlled X_ or _controlled NOT_.  It applies $X$ on $q_0$ only when $q_1 = \lvert 1 \rangle$. This is equivalent to the classical computation with $\texttt{XOR}$ gate if input qubits are either $\lvert 0 \rangle$ or $\lvert 1 \rangle$.   We can see the difference between classical and quantum computation  when a superposition state is used as input. Consider a case where $q_0=\lvert 0 \rangle$ and $q_1=c_0 |0 \rangle + c_1 \lvert 1 \rangle$.  The state of the two qubits is
# 
# $$
# \lvert \Psi_\text{in} \rangle = \lvert 0 \rangle \otimes (c_0 \lvert 0 \rangle + c_1 \lvert 1 \rangle) = c_0 \lvert 0 \rangle\otimes \lvert 0 \rangle + c_1 \lvert 0 \rangle \otimes \lvert 1 \rangle.
# $$
# 
# The output is
# 
# $$
# \lvert \Psi_\text{out} \rangle =  c_0 \lvert 0 \rangle \otimes \lvert 0 \rangle + c_1 \lvert 1 \rangle \otimes \lvert 1 \rangle,
# $$
# 
# which is known as  _entangled_ state.   There is no way to express this state in a classical computer.  Quantum computation utilizes entangled states.
# 

# ## Readouts
# 
# When a qubit is in $\lvert 0 \rangle$ or $\lvert 1 \rangle$, readout is in principle accurate (not on current NISQ computers due to device errors). However, the outcome is completely uncertain if the qubit is in a superposition state {eq}`eqn:superposition`. We will obtain $\texttt{0}$ or $\texttt{1}$ at random.  If we prepare many qubits in the same superposition state, we obtain $\texttt{0}$ from some and $\texttt{1}$ from others. Hence, the readout of qubits is stochastic, from which we know that the qubits are in a superposition state but which one?  The principle of quantum mechanics tells us that the probability of getting $\texttt{0}$ is given by $|c_0|^2$ and $\texttt{1}$ by $|c_1|^2$.  By measuring many qubits in the same state, we can calculate the probabilities from which $|c_0|^2$ and $|c_1|^2$ can be determined.  The phase of $c_0$ and $c_1$ are still missing.  There is a complicate procedure, known as _quantum tomography_, which can determine the superposition state if and only if sufficiently large number of the same superposition states are measured.  Therefore, it is necessary to repeat the same quantum computation many times if the final result is a superposition state.  Even when the result of the computation is designed to be $\lvert 0 \rangle$ or $\lvert 1 \rangle$ by the algorithm, the outcome can be a superposition state due to device errors.  Even worse, the final state can be so-called _mixed state_, which contains a mixture of classical and quantum uncertainties simultaneously.  A good quantum circuit avoids both classical and quantum uncertainties as much as possible.

# 
# ---
# 
# Last modified on 08/30/2022.

# In[ ]:




