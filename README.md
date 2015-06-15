Puppet: Structured data with Hiera and the ENC's
================================================

## Intention
Describe structured data in puppet, how to get the data into puppet and how to use that data.
Note these examples make use of auto lookups.

This is not intended to describe how to setup puppet or a puppet master.

# What is this ENC thing ?
* An ENC is an External Node Classifier.
* It is an executable that is run on the puppet master with the FQDN (Fully Qualified Domain Name) of the node it is serving as the only argument.
* It should return YAML (Yet Another Markup Language / YAML Aint Markup Language depending on who you listen to)
* It can be any thing with the 'x' bit set that returns yaml as above. so could be Ruby, Python, Java or any other language you can get to run on your Puppet Master

The [Puppet ENC Documentation](https://docs.puppetlabs.com/guides/external_nodes.html) is well worth a read.

# What's (with) Structured Data
For those who aren't familiar with the term, you may know it as a hash or array of arrays. To help visualize, if you think of excel   the Cell A1 contains a value, A2 another, B2 yet another etc. Structed data is just thinking of this in terms of the whole sheet, or for preference the whole workbook.

## How is structed data used ?
Typically in puppet the data is stored in hiera, the heirachy (as typically configured in /etc/puppet/hiera.yaml) will typically have been 3 and 10 levels. When the puppet master searches for data
The idea is instead of doing a lookup for A1, and then another for each cell we only perform one lookup (for sheet1, or workbook1) and then where needed. The key point is all of the data is related (see hiera/data.yaml)

## How would I use an ENC
To add an ENC to a Puppet master it's just a few lines under the [master] directive
```
[master]
  node_terminus     = exec
  external_nodes    = /path/to/your/enc
```

## So why would I move my data from Hiera to an ENC ?
* Let others manage the data. After all most of the time they are / should be responsible for that data eg
  * A Python app querrying a MySQL database on the puppet master side
  * A Java app providing the GUI API to the DB.
* Have the Release team decide which versions of an application should be in an the test / pre-production and production environments
* Have the Dev Team(s) decide which versions should be in the Dev / Integration environments
* Have your build management update what packages are available to each environment

#### Simply put it can be used to hand the data to others
Why should anyone have to make a pull request to update a package version? Isn't that a waste of everone's time ?
