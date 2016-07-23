# Maintaining your own channel

What if you have a project with a bunch of dependencies?

 * They are not all in the default channel
 * You may be maintaining a few of them yourself
 * They are not all easy to build.

How do you make it easy for your users to use your project?

# enter `anaconda.org` channels

ancaonda.org provides a number of services

One of them is hosting "channels" were you can put your own collection of conda packages.

If you put all the uncommon dependencies your project needs in one channel, you users only need to:

1) install miniconda:

http://conda.pydata.org/miniconda.html

2) add your channel:

conda add 
