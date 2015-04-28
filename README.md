# awesome-mysql

A curated list of awesome MySQL software, libraries and resources.

This list accepts and encourages pull requests. See [CONTRIBUTING](CONTRIBUTING.md)

The initial commit for this list is deliberatly incomplete, in the intention that the community assists in shaping the list.

### Contents

- [Awesome MySQL](#awesome-mysql)
    - [Analysis](#analysis)
    - [Backup](#backup)
    - [ChatOps](#chatops)
    - [Connectors](#connectors)
    - [Deployment](#deployment)
    - [Development](#development)
    - [GUI](#gui)
    - [HA](#ha)
    - [Proxy](#proxy)
    - [Replication](#replication)
    - [Schema](#schema)
    - [Server](#server)
    - [Sharding](#sharding)
    - [Toolkits](#toolkits)

- [Resources](#resources)
    - [Conferences](#conferences)
    - [E-Books](#e-books)
    - [Media](#media)
    - [Newsletters](#newsletters)


## Analysis

*Performance, structure & data analysis tools*

- [Anemometer](https://github.com/box/Anemometer) - Box SQL slow query monitor.
- [innodb-ruby](https://github.com/jeremycole/innodb_ruby) - A parser for InnoDB file formats, in Ruby.
- [innotop](https://github.com/innotop/innotop) - a 'top' clone for MySQL with many features and flexibility.
- [pstop](https://github.com/sjmudd/pstop) - a top-like program for MySQL, collecting, aggregating and displaying information from performance_schema.


## Backup

*Backup/restore/recovery tools*

- [MyDumper](https://launchpad.net/mydumper) - Logical, parallel backup/dumper tool for MySQL
- [Percona Xtrabackup](http://www.percona.com/doc/percona-xtrabackup) - an open-source hot backup utility for MySQL - based servers that doesn’t lock your database during the backup.

## ChatOps

*Scripts integrated into chat rooms*

- [Hubot MySQL ChatOps](https://github.com/samlambert/hubot-mysql-chatops)

## Connectors

*MySQL connectors for various programming languages*

- [Connector/Python](https://dev.mysql.com/downloads/connector/python/) - a standardized database driver for Python platforms and development.
- [go-sql-driver](https://github.com/go-sql-driver/mysql) - a lightweight and fast MySQL-Driver for Go's (golang) database/sql package.
- [MySQL-Python](http://sourceforge.net/projects/mysql-python/) - MySQL database connector for Python programming.


## Deployment

*MySQL deployment tools*

- [MySQL Sandbox](http://mysqlsandbox.net/) - a tool that installs one or more MySQL servers within seconds, easily, securely, and with full control.


## Development

*Tools to support MySQL-related development*

- [Flywaydb](http://flywaydb.org/getstarted/) - Database migrations; Evolve your database schema easily and reliably across all your instances
- [Liquibase](http://www.liquibase.org/) - Source control for your database
- [Propagator](https://github.com/outbrain/propagator) - Centralized schema & data deployment on a multi-everything topology


## GUI

*GUI frontends & applications*

- [HeidiSQL](http://www.heidisql.com/) - MySQL GUI frontend for Windows.
- [MySQL Workbench](http://dev.mysql.com/downloads/workbench/) - provides DBAs and developers an integrated tools environment for database design & modeling; SQL devleopment; database administration.
- [phpMyAdmin](http://www.phpmyadmin.net/home_page/) - a free software tool written in PHP, intended to handle the administration of MySQL over the Web.
- [SequelPro](https://github.com/sequelpro/sequelpro) - a fast, easy-to-use Mac database management application for working with MySQL databases.


## HA

*High availability solutions*

- [Galera Cluster](http://galeracluster.com/products/) - a true Multimaster Cluster based on synchronous replication.
- [MHA](http://code.google.com/p/mysql-master-ha/) - Master High Availability Manager and tools for MySQL
- [MySQL Fabric](https://www.mysql.com/products/enterprise/fabric.html) - an extensible framework for managing farms of MySQL Servers.


## Proxy

*Proxies to MySQL*

- [MaxScale](https://github.com/mariadb-corporation/MaxScale) - open-source, database-centric proxy.
- [MySQL Proxy](https://launchpad.net/mysql-proxy) - A simple program that sits between your client and MySQL server(s) that can monitor, analyze or transform their communication.
- [ProxySQL](https://github.com/renecannao/proxysql) - High performance proxy for MySQL.


## Replication

*Replication related software*

- [orchestrator](https://github.com/outbrain/orchestrator) - MySQL replication topology management and visualization tool.
- [Tungsten Replicator](http://code.google.com/p/tungsten-replicator/) - A high performance, open source, data replication engine for MySQL.


## Schema

*Add-on schemas*

- [common_schema](http://code.google.com/p/common-schema/) - DBA's framework for MySQL, providing a function library, views library and QueryScript interpreter.
- [sys](https://github.com/MarkLeith/mysql-sys) - A collection of views, functions and procedures to help MySQL administrators get insight in to MySQL Database usage.


## Server

*MySQL server flavors*

- [MariaDB](https://github.com/MariaDB/server) - Community developed fork of MySQL server.
- [MySQL Server & MySQL Cluster](https://github.com/mysql/mysql-server) - Official Oracle's MySQL server & MySQL Cluster distribution.
- [Percona Server](https://launchpad.net/percona-server) - An enhanced, drop-in MySQL replacement.
- [WebScaleSQL](https://github.com/webscalesql/webscalesql-5.6) - WebScaleSQL, Version 5.6, based upon the MySQL-5.6 community releases.


## Sharding

*Sharding solutions/frameworks*

- [vitess](https://github.com/youtube/vitess) - vitess provides servers and tools which facilitate scaling of MySQL databases for large scale web services.
- [jetpants](https://github.com/tumblr/jetpants) - An automation suite for managing large range sharding clusters, by Tumblr.


## Toolkits

*Toolkits, general purpose scripts*

- [Percona Toolkit](http://www.percona.com/software/percona-toolkit) - a collection of advanced command-line tools to perform a variety of MySQL server and system tasks that are too difficult or complex to perform manually.
- [UnDROP](https://twindb.com/undrop-tool-for-innodb/) - a tool to recover data from dropped or corrupted InnoDB tables.

# Resources

*At this stage "resources" will not include websites, blogs, slides, presentation videos, etc. in fear of list size*

##Conferences

*Public, recurring conferences on and around MySQL*

- [FOSDEM](https://fosdem.org/) - a free event for software developers to meet, share ideas and collaborate. Annually, in Brussels. Offers "MySQL & friends" room.
- [MySQL Central](https://www.oracle.com/openworld/mysql/index.html) - Oracle's annual MySQL conference, as part of Oracle Open World.
- [Percona Live](http://www.percona.com/live/conferences) - MySQL & Openstack focused conference.


## Media

*Public, ongoing video & audio casts. This excludes conference presentations in fear of list size*

- [DBHangOps](http://dbhangops.github.io/) - a bi-weekly google hangout meeting of various members of the MySQL community that simply want to talk shop about MySQL in their day-to-day .
- [OurSQL Podcast](http://www.oursql.com/) - The MySQL database community podcast.


## Newsletters

*Newsletters require an email address, by definition. List below are newsletters that require nothing but an email address*

- [Weekly MySQL News](http://mysqlnewsletter.com/) - Unofficial weekly news digest of all things MySQL.
