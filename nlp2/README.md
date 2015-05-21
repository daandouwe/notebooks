# NLP2

These are notebooks I've put together for UvA's NLP-2 course.

## Requirements

The notebook about permutations with FSA interfaces the amazing `openfst` library and it does so by using Victor Chahuneau's very fine python wrapper:

* [pyfst](https://github.com/clab/pyfst)
  * instead of cloning it from Victor's github, we are using `clab`'s fork because the latter has been updated to work with the most recent distribution of `openfst`
  * [general instructions](http://demo.clab.cs.cmu.edu/fa2014-11711/index.php/PyFST_Setup)
  * [mac](http://demo.clab.cs.cmu.edu/fa2014-11711/index.php/PyFST_Setup_Mac)
  * [tutorial](http://demo.clab.cs.cmu.edu/fa2013-11711/images/7/7d/OpenFST_Tutorial.pdf) for those who want to learn more about `pyfst`

The notebook about binarizable permutations requires a chart parser

* [Earley parser](https://github.com/wilkeraziz/pcfg-sampling.git)
  * all you need to do is to git-clone this repo and add it to your `PYTHONPATH` before starting the notebook

* `networkx` and `nxpd` for drawing hypergraphs
      pip install pygraphviz
      pip install networkx
      pip install nxpd
