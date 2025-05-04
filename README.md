# Task-Ordering

Suppose you have a project consisting of a series of steps, and you have requirements about which steps must
be finished before others can begin. Each step is designated by a single capital letter. For example, suppose you
have the following instructions:

Step C must be finished before step A can begin.  
Step C must be finished before step F can begin.  
Step A must be finished before step B can begin.  
Step A must be finished before step D can begin.  
Step B must be finished before step E can begin.  
Step D must be finished before step E can begin.  
Step F must be finished before step E can begin.  

These requirements can be represented by a list of two-item lists, with each two-item list’s first element representing
a task that must precede a task listed as the second element. For example, the network described above
could be represented in Python as:

rule_list = [ [’C’,’A’], [’C’,’F’], [’A’,’B’], [’A’,’D’], [’B’,’E’], [’D’,’E’], [’F’,’E’] ]

Note that the order of the two-item lists within the outer list of lists is not important.
Your task is to create a Python module called sorted.py containing a function called sorted steps() that takes
a list of lists formatted as above that define the step ordering rules as the sole user-provided argument. Whenever
there are multiple steps that could legally be yielded (i.e.,whose prerequisite steps have been completed),
yield the step that is first in alphabetical order. The function must return a string consisting of the letters corresponding
to each step, in an order that satisfies all the conditions. It must contain each step mentioned in a rule,
and each of these exactly once.  

For example, consider the following code:

from sorted import sorted_steps

rule_list = [ [’C’,’A’], [’C’,’F’], [’A’,’B’], [’A’,’D’], [’B’,’E’], [’D’,’E’], [’F’,’E’] ]
step_string = sorted_steps(rule_list)
print(step_string)

An example of a string that violates the ordering constraint is CDFABE: this violates the rule step A must be
finished before step D can begin. All the strings CABDFE, CFADBE, and CAFDBE satisfy the ordering constraints,
but the only one that also satisfies the alphabetization constraint is CABDFE.
