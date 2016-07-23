% Conda-forge
% A community powered conda packaging
% July 23th 2016

---

# Who am I?

- [Chris Barker](https://github.com/pythonCHB)

- Work for [NOAA](http://response.restoration.noaa.gov)
- Managing a [complex project(s) with lots of ugly dependencies:](https://github.com/NOAA-ORR-ERD/PyGnome/blob/master/conda_requirements.txt)
- Maintaining a anaconda [channel with our dependencies](https://anaconda.org/noaa-orr-erd)

- I learned a lot from: [Filipe Fernandes](https://github.com/ocefpaf)
- And the [IOOS conda channel](https://github.com/ioos/conda-recipes/wiki)

Now switching to the [conda-forge](https://conda-forge.github.io/) community channel

Much thanks to Filipe Fernandes and Phil Elson of the UK met office for these slides (and conda-forge)

# Some more background and motivation

A post about it from Wes Mckinney:

[http://wesmckinney.com/blog/conda-forge-centos-moment](http://wesmckinney.com/blog/conda-forge-centos-moment)


And one from the conda forge community:

[https://www.continuum.io/blog/developer-blog/community-conda-forge](https://www.continuum.io/blog/developer-blog/community-conda-forge)

# The problem

The Python scientific community always wanted a package manager that is cross platform,
does not require sudo, and lets Python be awesome.

The conda package manager solved that problem, but created a new ones.

. . .

> - How do I get software that is not in the `defaults` channel?
> - If I build my own binaries where should I host them?
> - How should I build them to ensure they are compatible with other systems and the default channel?

# More about the problem

The `defaults` cannot keep up with the pace of the scientific community and many users/communities channels were created to fill in that gap.

That led to duplication of effort, recipe fragmentation, unstable environments when mixing and matching packages from different channels, etc.

# Let's take a step back: what is a conda channel?

> - Is similar to a Linux repository (or app store)
> - The service is hosted for free at Continuum's Anaconda Cloud (https://anaconda.org)
> - We can upload pre-compiled binaries using the `conda` package manager

# We've already covered conda ...

But here's a reminder:

> - An open-source packaging system developed for, and used by, the scientific software community.
> - Also useful for everyone else!
> - From their own webpage:
> - "Package Everything!"
> - "And share your repositories with clients or colleagues."


# Why use conda?

> - Reproducible environments are easy to create
> - Better solution than wheels for Python packages that depend on external libraries
> - One approach for multiple platforms (no `apt-get`, `yum`, `brew`, etc)

. . .

[http://technicaldiscovery.blogspot.com.br/2013/12/why-i-promote-conda.html](http://technicaldiscovery.blogspot.com.br/2013/12/why-i-promote-conda.html)

# The solution

The conda-forge organization was created to be transparent, open and community
led with the goal of building conda packages and providing a stable source for
packages while reducing the effort duplication and recipe fragmentation.

. . .

While developed to meet the unique needs of scientific software developers,
it is a system that brings features and utilities for the broader developer community.

# What do we mean by community?

Having a community-governed package channel for conda and a community process for submitting, verifying, and storing *signed* project releases

[https://conda-forge.github.io/](https://conda-forge.github.io/)

# The conda-forge [channel](http://anaconda.org/conda-forge)

> - over 70 contributors
> - 866 packages
> - Available platforms are: Linux-64, Windows-32/64, and OS X
> - You can install with `conda install -c conda-forge a_package`

# Builds

> - The recipes are hosted on [GitHub](https://github.com/conda-forge/feedstocks/tree/master/feedstocks)
> - [AppVeyor](http://www.appveyor.com/) &#10139; Windows
> - [Travis-CI](https://travis-ci.org/) &#10139; OSX
> - [CircleCI+Docker](https://registry.hub.docker.com/u/ocefpaf/centos64-conda-obvious-ci/) &#10139; Linux (CentOS 5)

# [Automation](https://github.com/conda-forge/conda-forge.github.io/tree/master/scripts)

> - The point of entry is [staged-recipes](https://github.com/conda-forge/staged-recipes)
> - The tooling lives in [conda-smithy](https://github.com/conda-forge/conda-smithy)
> - Once the PR is accepted a GitHub team is created based on the maintainers list
> - The maintainers have commit rights only to their own recipes

# [Linter](https://github.com/conda-forge/conda-forge-webservices/tree/master/conda_forge_webservices)

![](images/github_linter.png)

# Issues

![](images/github_issues.png)

# How to use the channel?

```bash
conda config --add channels conda-forge

conda env create environment.yml
```

or

```bash
conda install something
```

or, if you don't want the channel to be there by default:

```bash
conda install -c conda-forge something
```

. . .

**That is it!**


# An Example Environment File

```yaml
name: geopython
channels:
    - conda-forge
dependencies:
    - python=2.7
    - jupyter
    - matplotlib
    - gdal
    .
    .
```

# How to contribute?

> - Report problems
> - Request packages or new releases
> - Send PRs adding/fixing packages
> - Submit your own packge to manage

. . .

All with the gitHub "workflow"


# Submitting a New Recipe

1. Fork [https://github.com/conda-forge/staged-recipes](https://github.com/conda-forge/staged-recipes)
2. Create a branch for your recipe (you only want one recipe per PR)
3. Submit the PR -- The recipe will be built and, once merged, it will trigger the creation of the feedstock repository
4. In the feedstock repo, the recipe will be re-built and uploaded to the conda-forge channel on anaconda.org

You will then be a maintainer of that recipe -- and can update, etc. without any intervention by the core maintainers.

# Creating a [recipe](https://github.com/conda-forge/staged-recipes/tree/master/recipes/example)

```yaml
{% set version = "1.0" %}

package:
  name: example
  version: {{ version }}

source:
  fn: example-{{ version }}.tar.gz
  url: https://pypi.python.org/example-{{ version }}.tar.gz
  sha256: 842b44f8c95517ed5b792081a2370da1

build:
  number: 0
  script: pip install --no-deps ./

requirements:
  build:
    - python
    - pip
  run:
    - python

test:
  requires:
    - pytest
  imports:
    - example
  commands:
    - py.test --pyargs example

about:
  home: https://example.com/examples/
  license: BSD 3-Clause
  summary: An example package

extra:
  recipe-maintainers:
    - <GitHubHandle>

```

# The truth about creating recipes

> - `conda skeleton pypi <packages>`
> - [Search](http://anaconda.org/search?q=gsw), download, copy, and paste
> - Find a similar "feedstock" on conda-forge github and copy it.

. . .

Note: you may be better off working with [the conda-forge example recipe](https://github.com/conda-forge/staged-recipes/blob/master/recipes/example/meta.yaml)


# Maintaining recipes in the feedstock

```yaml
{% set version = "1.0" %}

package:
  name: example
  version: {{ version }}

source:
  fn: example-{{ version }}.tar.gz
  url: https://pypi.python.org/example-{{ version }}.tar.gz
  md5: 842b44f8c95517ed5b792081a2370da1
  patches:
    - some.patch

build:
  number: 0
  .
  .
  .
```

# Maintenance example part 0: the PR

![](images/github_maintaince.png)

# Maintenance example part 1: the actual changes

![](images/github_maintaince_changes.png)


# Maintenance example part 2: provenance

![](images/github_provenance.png)

# How to find [us](https://github.com/orgs/conda-forge/people)?

[Github](https://github.com/conda-forge)

[Gitter](https://gitter.im/conda-forge/conda-forge.github.io)

[Mailing list](https://groups.google.com/forum/#!forum/conda-forge)

# Other tools from conda-forge

Conda-forge is really two things:

 - a community-maintained repository of conda packages
 - a set of tools that faciliate building conda pacakges

Some of those tools are useful on there own.

## `conda-build-all`

`conda-build all`: https://github.com/SciTools/conda-build-all

is a add-on for conda that facilitates the building of multiple conda packages accross a "matrix" of python and numpy versions.

with one command, you can build an entire set of packages, and upload them to your own anaconda.org channel:

```
$ conda-build-all my_recipes --matrix-condition "python 3.5.*" "numpy >=1.8"
```

This is very useful for providing a custom channel of pacakges for your project:

https://github.com/NOAA-ORR-ERD/orr-conda-recipes




# Questions?

![](http://imgs.xkcd.com/comics/tools.png)

[http://xkcd.com/1629/](http://xkcd.com/1629/)
