

# Apache Spark

Apache Spark is an open source cluster computing framework. Originally developed at the University of California, Berkeley's AMPLab,
the Spark codebase was later donated to the Apache Software Foundation that has maintained it since. Spark provides an interface
for programming entire clusters with implicit data parallelism and fault-tolerance.

# Overview

# RDD (Resilient Distributed Dataset)
 - Apache Spark provides programmers with an API centered on a data structure called RDD.
 - It is a read-only multiset of data items distributed over a cluster of machines, that is maintained in fault-tolerant way.
 - It was developed in response to limitations in the MapReduce cluster computing paradigm, which forces a particular linear dataflow structure on distributed programs.
 - MapReduce programs read input data from disk, map a function across the data, reduce the results of the map, and store reduction results on disk. 
 - Spark's RDDs function as a working set for distributed programs that offers a (deliberately) restricted form of distributed shared memory.

# Strong at Iterative algorithms

The availability of RDDs facilitate the implementation of both iterative algorithms, that visit their dataset multiple times in a loop,
and interactive/exploratory data analysis, the repeated database-style querying of data.

Among the class of iterative algorithms are the training algorithms for machine learning systems, which formed the initial impetus for
developing Apache Spark.


# Cluster manager and Distributed storage system

Apache Spark requires a cluster manager and a distributed storage system.

For cluster management,
 Spark supports standalone (native Spark cluster), Hadoop YARN, or Apache Mesos.

For distributed storage,
 Spark can interface with a wide variety, including Hadoop Distributed File System (HDFS), MapR File System (MapR-FS),
Cassandra, OpenStack Swift, Amazon S3, Kudu, or a custom solution can be implemented.

Spark also supports a pseudo-distributed local mode, usually used only for development or testing purposes, where distributed storage is not required
and the local file system can be used instead; in such a scenario, Spark is run on a single machine with one executor per CPU core.

# Spark Core

Spark Core => responsible for distributed task dispatching, scheduling, and basic I/O functionalities, 
exposed through an API (for Java, Python, Scala, and R) centered on the RDD abstraction. 

This interface mirrors a functional/high-order model of programming:
a "driver" program invokes parallel operations such as map, filter or reduce on an RDD by passing a function to Spark, which then schedules the function's
execution in parallel n the cluster. These operations, and additional ones such as joins, take RDDs as input and produce new RDDs.

# Lazy evaluation and Fault-tolerance

RDDs are immutable and their operations are lazy;
fault-tolerance is achieved by keeping track of the "lineage" of each RDD (the sequence of operations that produced it)
so that it can be reconstructed in the case of data loss. 
RDDs can contain any type of Python, Java, or Scala objects.

Aside from the RDD-oriented function style of programming, 
Spark provides two restricted forms of shared variables:
 - broadcast variables
 - accumulators

broadcast variables reference read-only data that needs to be available on all nodes,
while accumulators can be used to program reductions in an imperative style.

A typical example of RDD-centric functional programming is the following Scala program that computes the frequencies of all words occuring in a set of 
text files, and prints the most common ones. Each map, filterMap and reduceByKey takes an anonymous function that performs a simple operation on 

# Lambda function

lambda function => anonymous function
