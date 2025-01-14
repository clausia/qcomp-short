#!/usr/bin/env python
# coding: utf-8

# (sec-qinfo)=
# # Quantum Information Theory

# ## Classical information
# 
# We  ask a question because we do not know something and try to find it.  In other words, we try to get new [information](https://en.wikipedia.org/wiki/Information).  But what is information and can we quantify the amount of information?  To answer this question, [information theory](https://en.wikipedia.org/wiki/Information_theory) was developed in the first half of twenty century by [Claude Shannon](https://en.wikipedia.org/wiki/Claude_Shannon) and others.  
# 
# In essence,  the amount of information we obtain is the amount of uncertainty decreased.  If there is no uncertainty, there is nothing to ask.  The uncertainties arise in several different ways.  The outcome of an event that is going to happen in future can be uncertain if we cannot predict it precisely.  The uncertainty is mainly due to the stochastic nature of the event, e.g. rolling a die.  In another case, an event has already happened and some people know the outcome.  For those who dont' know it, the outcome is uncertain but it is due to their ignorance.  In either case,  once the outcome is known, the uncertainty disappears and some information is gained.
# 
# The uncertainty can be mathematically expressed as probability.  Consider coin tossing. No one knows the outcome.  However, we know that it must be either head or tail.  We cannot predict the outcome because the motion of the coin is chaotic and thus the outcome is stochastic.  Assuming the coin is ideal, the probability of finding head and tail are equal, that is $p_\text{head} = \frac{1}{2}$ and $p_\text{tail}=\frac{1}{2}$. Shannon defined the amount of the information (undertainty) by
# 
# $$
# H = - p_\text{head} \log p_\text{head} - p_\text{tai} \log p_\text{tail} = \log 2
# $$
# 
# which is known as [*Shannon entropy*](https://en.wikipedia.org/wiki/Entropy_(information_theory)) or *information entropy*.  If base 2 is used, $\log_2 2 = 1$ and  we say one *bit* of information is gained.  Here *bit* is the unit of information. 
# 
# Even after the coin is tossed and landed on someone's hand,  the outcome is not known to us until the person shows it to others.  In this case, the uncertainty is due to ignorance but the amount of information we will find still one bit.
# 
# Here is the general definition of the Shannon entropy
# For a set of all possible outcomes, $\{\omega_1, \omega_2, \cdots, \omega_N\}$ where $N$ is the total number of possible outcomes and the probability $p_i$ of finding the outcome $\omega_i$ for all $i$ is defined,  the amount of  information  is measured by
# 
# $$
# H = - \sum_{i=1}^N p_i \log p_i.
# $$

# ## Quantum Information
# 
# Recall that information is about uncertainty or probability.  a classical bit is dichotomous and there is only one uncertainty, 0 or 1.  In contrast, the state of a qubit is continuous.  Does this mean a qubit contains infinite amount of information? It turns out that we can ask only a dichotomous question at a time.  
# 
# Consider a qubit in a superposition state
# 
# $$
# \lvert \psi \rangle = \frac{1}{\sqrt{2}} \lvert 0 \rangle +  \frac{1}{\sqrt{2}} \lvert 1 \rangle
# $$
# 
# When we ask if the qubit is in $\lvert 0 \rangle$, the answer is either "yes" or "no" but there is no definite answer.  There is 50% chance to get "yes" and 50% chance to get "no".  The situation is quite similar to the coin tossing.  
# 
# However, there are differences. You can ask a different question for a qubit.  Is the state $\lvert + \rangle =  \frac{1}{\sqrt{2}} \lvert 0 \rangle +  \frac{1}{\sqrt{2}} \lvert 1 \rangle$ or $\lvert - \rangle =  \frac{1}{\sqrt{2}} \lvert 0 \rangle -  \frac{1}{\sqrt{2}} \lvert 1 \rangle$?   Now, the answer is "yes" without ambiguity.  For this question,  $\lvert \psi \rangle$ contains no information!   Although the question we can ask is always dichotomous, we can ask infinitely many different questions.  This is the main difference between qubit and classical bit.
# 
# Even when we know precisely that the qubit is in the state $\lvert \psi \rangle$, there is still the uncertainty, not due to our ignorance nor due to future event since $\lvert \psi \rangle$ already exists. and we know it.  Nevertheless, the amount of information seems $\log 2$. The uncertainty is originated from the quantum measurement which is inherently stochastic.  The measurement is supposed to gain information and thus uncertainty should decrease but the very process to extract information creates uncertainty!  
# 
# The no-teleportation theorem suggests that infinitely many classical bits are needed to describe the state of a single qubit.  Nonetheless, we can extract only one classical bit of information out of it.  This is known as [*Halevo bound*](https://en.wikipedia.org/wiki/Holevo%27s_theorem).  If you have $n$ qubits, you can get only $n$ classical bits of information.  On the other hand, we can transmit two classical bits of information using a single qubit, which is known as [*superdense coding*](https://en.wikipedia.org/wiki/Superdense_coding).  The trick is to use quantum entanglement as resource.
# 
# We define quantum information entropy using density operator $\rho = \lvert \psi \rangle \langle \psi \rvert$ as
# 
# $$
# S = - \text{Tr} \left(\rho \log \rho\right)
# $$
# 
# which is known as von-Neumann entropy. Plugin $\rho = \lvert \psi \rangle \langle \psi \rvert$ , we find $S=0$.  Hence, the state has no information (uncertainty) with respect to the question "what is the state of qubit?".  We know the answer prcesiely. It is $|\psi\rangle$. When quantum measurement is done, the state collapses to a different state, which can have a non-vanishing information classical Shannon entropy.  In this sense, classical information is created out of quantum information, when measurement is done.  For the current example, the state after measurement of $\lvert 0 \rangle$ and $\lvert 1 \rangle$, the state after the non-selective measurement is
# 
# $$
# \rho = \frac{1}{2}  \lvert 0 \rangle \langle 0 \rvert + \frac{1}{2}  \lvert 1 \rangle \langle 1 \rvert
# $$
# 
# and its von Neumann entropy is $S = \log 2$ as expected. 
# 

# ## Restriction on quantum information processes
# 
# Qubits have many advantages over classical bits, which is the main topics of this book.  However, they have also many disadvantages.  Here are some restrictions imposed on the quantum information.
# 
# 1. [**No-cloning theorem**](https://en.wikipedia.org/wiki/No-cloning_theorem)  
# The theorem states that it is not possible to duplicate an arbitrary qubit.   During quantum computation we cannot make a copy of a qubit in an unknown state.  Recall that classical bit can be cloned.
# 
# 2. [**No-teleportation theorem**](https://en.wikipedia.org/wiki/No-teleportation_theorem)  
# If the information stored in a qubit can be converted to a classical bit string and vice versa, we can *teleport* the quantum information to a distant place via a classical bit string. Such teleportation is not possible.  This theorem imposes more important restriction.  We cannot read out the full information in an arbitrary qubit since the outcome of the measurement is classical.
# 
# 3. [**No-deleting theorem**](https://en.wikipedia.org/wiki/No-deleting_theorem)  
# If two qubits happened to be in the same but arbitrary state, it is not possible to delete the information in one of the qubits.  This is a no-go theorem and time-reversal of no cloning theorem.
# 
# 4. [**No-broadcasting theorem**](https://en.wikipedia.org/wiki/No-broadcasting_theorem)  
# It is possible to transfer the full information in an arbitrary qubit to another qubit but the information in the original qubit must be destroyed.  This is known as *quantum teleportation*.  However, broadcasting the full information in an arbitrary qubit to multiple qubits is not possible. This is a corollary of no cloning theorem.
# 
# 5. [**No-hiding theorem**](https://en.wikipedia.org/wiki/No-hiding_theorem)  
# Briefly stating, the information stored in quantum system must be conserved. It is not possible to create or destroy quantum information.  In contrast, classical information can be created or destroyed.
# 
# 

# 
# ---
# 
# Last modified on 08/30/2022.
# 
