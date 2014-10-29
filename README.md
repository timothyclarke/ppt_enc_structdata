Puppet: Structured data with Hiera and the ENC's
================================================

## Intention
Describe structured data in puppet, how to get the data into puppet and how to use that data.

This is not intended to describe how to setup puppet or a puppet master.

# What is this ENC thing ?
* An ENC is an External Node Classifier.
* It is an executable that is run on the puppet master with the FQDN (Fully Qualified Domain Name) of the node it is serving as the only argument.
* It should return YAML (Yet Another Markup Language / YAML Aint Markup Language depending on who you listen to)

The [Puppet ENC Documentation](https://docs.puppetlabs.com/guides/external_nodes.html) is well worth a read.

# What's (with) Structured Data
For those who aren't familiar with the term, you may know it as a hash or array of arrays. To help visualize, if you think of excel   the Cell A1 contains a value, A2 another, B2 yet another etc. Structed data is just thinking of this in terms of the whole sheet, or for preference the whole workbook.

## How is structed data used ?
Typically in puppet the data is stored in hiera, the heirachy (as typically configured in /etc/puppet/hiera.yaml) will typically have been 3 and 10 levels. When the puppet master searches for data
The idea is instead of doing a lookup for A1, and then another for each cell we only perform one lookup (for sheet1, or workbook1) and then where needed. The key point is all of the data is related (see hiera/data.yaml)

