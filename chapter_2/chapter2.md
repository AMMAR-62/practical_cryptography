## MD5 Algorithm:
-  md stands for message digest.
-  a digest - converts a document of any length (even an empty document) into a large number that takes up a fixed amount of space.
-  Features of a digest:
  - the same document always produces the same digest.
  - the digest "feels" random: if you have a digest, it gives you no clues about the documents.
  - Digest works the same way as fingerprint, if you have a person at hand, it's easy to produce a (relatively) consistent and unique fingerprint; but if the only thing you have is a fingerprint, it's not so easy to find out who it is.
  - Hash functions are lossy, this is critical to their function, because without a loss of information, there would be a way to go from the has to the document.
  - A simple example of hash is even or odd which is sometimes called a parity bit and has often been used as a rudimentary error detection code.
  - All hash functions have the fundamental qualities of consistency, compression, and lossiness and have all kinds of important applications in computer science.
  - for a hash function to be cryptographic or secure it needs to be have:
    - Preimage resistance.
    - Second-preimage resistance.
    - Collision resistance.
  ---
**Preimage resistance:**
 - preimage is the set of inputs for a hash function that produce a specific output
```
  Preimage: A preimage for a hash function H and a hash value k is the set of values of x for which H(x) = k.
```
 - **The idea of preimage resistance is basically this:** if you hand me a digest and I don’t 
already know how you got it, I can’t even find one element in the preimage for it without 
doing a ridiculous amount of work
 - The process of attempting to find an element in the preimage for a given output is 
called inverting the hash: 
- MD5 outputs a value in 16 bytes, which is 128 bits. With n bits we can express 2<sup>n</sup> individual values
- Even if you checked 1 million values per second (and were guaranteed that nothing you checked produced an output you had seen before), it would still take you about 1026 years (100 million billion billion!) to find a suitable input by brute force
---
**Second-Preimage resistance:**
 - if you already have one document that produces a particular digest, it’s still really hard to find a different document that produces that same digest
---
**Collision Resistance**
 -  it’s hard to find any two inputs that produce the same output: not a specific output, just the same output
 -  When a hash algorithm is resistant to collision, it is resistant to being able to purposefully create or pick any two inputs that produce the same digest, without deciding what that digest should be beforehand. 
---
**Avalanches property**
 - small changes in input can produce very large changes in output
 - This is due to a property shared by many hashes and cryptographic ciphers called the avalanche property
---
**Salting**
 - **Deterministic hacking**: hash maps to the SHA-256 of “password,” is still compromised
 - This is where the idea of a “salt” comes into play. 
 - **A salt is a publicly known value that is mixed in with the user’s password before hashing**
 - 
