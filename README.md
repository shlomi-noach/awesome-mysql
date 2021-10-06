# awesome-mysql

A curated list of awesome MySQL free and opensource software, libraries and resources. [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

This list accepts and encourages pull requests. See [CONTRIBUTING](https://github.com/shlomi-noach/awesome-mysql/blob/master/CONTRIBUTING.md)

### Contents

- [Awesome MySQL](#awesome-mysql)
    - [Analysis](#analysis)
    - [Backup](#backup)
    - [Benchmarking](#benchmarking)
    - [Binlog Replication](#binlog-replication)
    - [ChatOps](#chatops)
    - [Configuration](#configuration)
    - [Connectors](#connectors)
    - [Deployment](#deployment)
    - [Development](#development)
    - [GUI](#gui)
    - [HA](#ha)
    - [Proxy](#proxy)
    - [Replication](#replication)
    - [Schema](#schema)
    - [Security](#security)
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
- [MySQL Explain Analyzer](https://github.com/Preetam/explain-analyzer) - A web-based analyzer of `EXPLAIN FORMAT=JSON` output, providing comments, scalability analysis and permalinks for saved samples.
- [mysql-statsd](https://github.com/db-art/mysql-statsd) - A Python daemon to collect information from MySQL and send it via StatsD to Graphite.
- [MySQLTuner-perl](http://mysqltuner.com) - A script that allows you to review a MySQL installation quickly and make adjustments to increase performance and stability.
- [Percona Monitoring and Management](https://www.percona.com/doc/percona-monitoring-and-management/index.html) - An open-source platform for managing and monitoring MySQL performance.
- [Prometheus](https://prometheus.io/)/[mysqld_exporter](https://github.com/prometheus/mysqld_exporter) - Time series database for real-time monitoring and alerting.
- [pstop](https://github.com/sjmudd/ps-top) - a top-like program for MySQL, collecting, aggregating and displaying information from performance_schema.
## Backup

*Backup/restore/recovery tools*

- [Dumpling](https://github.com/pingcap/dumpling) - Logical, parallel backup/dumper tool for MySQL/TiDB written in GoLang - support csv format output and integrated as library
- [MyDumper](https://github.com/maxbube/mydumper) - Logical, parallel backup/dumper tool for MySQL
- [MySQLDumper](http://www.mysqldumper.net/) - open-source web based backup tool - useful for shared webhosting
- [Percona Xtrabackup](http://www.percona.com/doc/percona-xtrabackup) - an open-source hot backup utility for MySQL - based servers that doesn’t lock your database during the backup.

## Benchmarking

*Tools to stress your servers*

- [iibench-mysql](https://github.com/tmcallaghan/iibench-mysql) - Java based version of the Index Insertion Benchmark for MySQL/Percona/MariaDB.
- [go-tpc](https://github.com/pingcap/go-tpc) - A golang port of [TPCC](http://www.tpc.org/tpcc/) and [TPCH](http://www.tpc.org/tpch/) benchmark for MySQL.
- [Sysbench](https://github.com/akopytov/sysbench) - a modular, cross-platform and multi-threaded benchmark tool.
- [TPCC-MySQL](https://code.launchpad.net/~percona-dev/perconatools/tpcc-mysql) - A port of the popular [TPCC](http://www.tpc.org/tpcc/) benchmark for MySQL.

## Binlog-Replication

- [DM](https://github.com/pingcap/dm) - A High-Availability data migration platform which supports migrating data from MySQL/MariaDB to TiDB and merging shard tables
- [Kingbus](https://github.com/flike/kingbus) - A distributed MySQL binlog storage system built on Raft
- [mysql-ripple](https://github.com/google/mysql-ripple) - Ripple, a server that can serve as a middleman in MySQL replication

## ChatOps

*Scripts integrated into chat rooms*

- [Hubot MySQL ChatOps](https://github.com/samlambert/hubot-mysql-chatops)

## Configuration

*MySQL sample configuration and advisors*

- [mysql-compatibility-config](https://github.com/morgo/mysql-compatibility-config) - make MySQL configuration behave more like newer (or older) releases of MySQL.

## Connectors

*MySQL connectors for various programming languages*

- [Connector/C](https://dev.mysql.com/downloads/connector/c/) - Official C driver for MySQL.
- [Connector/CPP](https://dev.mysql.com/downloads/connector/cpp/) - Official C++ driver for MySQL.
- [Connector/J](https://dev.mysql.com/downloads/connector/j/) - a standardized database driver for the Java platforms and development.
- [Connector/Net](https://dev.mysql.com/downloads/connector/net/) - a standardized database driver for .Net platforms and development.
- [Connector/Node.js](https://dev.mysql.com/downloads/connector/nodejs/) - Official Node.js driver for MySQL.
- [Connector/Python](https://dev.mysql.com/downloads/connector/python/) - a standardized database driver for Python platforms and development.
- [DBD::mysql](https://metacpan.org/pod/DBD::mysql) - MySQL driver for the Perl5 Database Interface.
- [go-sql-driver](https://github.com/go-sql-driver/mysql) - a lightweight and fast MySQL-Driver for Go's (golang) database/sql package.
- [libAttachSQL](https://github.com/libattachsql/libattachsql) - libAttachSQL is a lightweight, non-blocking C API for MySQL servers.
- [MariaDB Java Client](https://mariadb.com/kb/en/mariadb/mariadb-connector-j/) - LGPL-licensed MariaDB Client Library for Java Applications.
- [mex-mariadb](https://github.com/markuman/mex-mariadb) - MIT licensed MariaDB/MySQL Client Library for GNU Octave and Matlab.
- [mysqlclient-python](https://github.com/PyMySQL/mysqlclient-python) - (Old) MySQL database connector for Python.
- [node-mysql](https://github.com/felixge/node-mysql) - A pure Nodejs Javascript client implementing the MySQL protocol.
- [PHP mysqlnd](https://dev.mysql.com/downloads/connector/php-mysqlnd/) - MySQL native driver for MySQL, deprecating older libmysql based driver.
- [PyMySQL](https://github.com/PyMySQL/PyMySQL) - MySQL database connector for Python.
- [Ruby Mysql2 gem](https://github.com/brianmario/mysql2) - MySQL driver for Ruby and Rails projects.

## Deployment

*MySQL deployment tools*

- [MySQL Docker](https://hub.docker.com/_/mysql/) - Official Docker images.
- [dbdeployer](https://www.dbdeployer.com) - A tool that installs one or more MySQL servers within seconds, easily, securely, and with full control.


## Development

*Tools to support MySQL-related development*

- [Flywaydb](http://flywaydb.org/getstarted/) - Database migrations; Evolve your database schema easily and reliably across all your instances
- [Liquibase](http://www.liquibase.org/) - Source control for your database
- [Shift](https://github.com/square/shift) - An application that helps you run schema migrations on MySQL databases
- [Skeema](https://www.skeema.io) - Declarative pure-SQL schema management system for MySQL and MariaDB, with support for sharding and external online schema change tools
- [Test database](https://github.com/datacharmer/test_db) - A sample MySQL database with an integrated test suite, used to test applications and servers


## GUI

*GUI frontends & applications*

- [Adminer](https://www.adminer.org/) - Database management in a single PHP file.
- [HeidiSQL](http://www.heidisql.com/) - MySQL GUI frontend for Windows.
- [mycli](https://github.com/dbcli/mycli) - A Terminal Client for MySQL with AutoCompletion and Syntax Highlighting.
- [MySQL Shell](https://dev.mysql.com/downloads/shell/) - Advanced client and code editor for MySQL that supports development and administration for the MySQL Server and MySQL InnoDB cluster (AdminAPI) with an interactive JavaScript, Python, or SQL interface.
- [MySQL Workbench](http://dev.mysql.com/downloads/workbench/) - provides DBAs and developers an integrated tools environment for database design & modeling; SQL devleopment; database administration.
- [Ocelot GUI](https://github.com/ocelot-inc/ocelotgui) - GUI client for MySQL or MariaDB, including debugger.
- [Percona Monitoring and Management](https://www.percona.com/doc/percona-monitoring-and-management/index.html) - An open-source platform for managing and monitoring MySQL performance.
- [phpMyAdmin](https://www.phpmyadmin.net/) - a free software tool written in PHP, intended to handle the administration of MySQL over the Web.
- [pspg](https://github.com/okbob/pspg) - provides a pager with enhanced visualization and navigation for tabular data. Originally implemented for PostgreSQL, but also supports MySQL.
- [Sequel Ace](https://github.com/Sequel-Ace/Sequel-Ace) - a Mac database management application for working with MySQL databases.
- [SQLyog Community edition](https://github.com/webyog/sqlyog-community/wiki/Downloads) - SQLyog Community edition. For Windows, works fine under wine in Mac and Linux
- [DBeaver](https://github.com/dbeaver/dbeaver) - A cross-platform SQL and NoSQL database client.
- [OmniDB/OmniDB: Web tool for database management](https://github.com/OmniDB/OmniDB)

## HA

*High availability solutions*

- [Galera Cluster](http://galeracluster.com/products/) - a true Multimaster Cluster based on synchronous replication.
- [MHA](http://code.google.com/p/mysql-master-ha/) - Master High Availability Manager and tools for MySQL.
- [orchestrator](https://github.com/github/orchestrator) - MySQL replication topology management and High Availability solution.
- [Percona Replication Manager](https://github.com/percona/percona-pacemaker-agents/) - Asynchronous MySQL replication manager agent for Pacemaker. Supports file and GTID based replication, geo-distributed clusters using booth.
- [replication-manager](https://github.com/signal18/replication-manager) - a high availability solution to manage MariaDB 10.x and MySQL & Percona Server 5.7 GTID replication topologies.

## Proxy

*Proxies to MySQL*

- [MaxScale](https://github.com/mariadb-corporation/MaxScale) - open-source, database-centric proxy.
- [Mixer](https://github.com/siddontang/mixer) - a MySQL proxy powered by Go which aims to supply a simple solution for MySQL sharding.
- [MySQL Proxy](https://launchpad.net/mysql-proxy) - A simple program that sits between your client and MySQL server(s) that can monitor, analyze or transform their communication.
- [ProxySQL](https://github.com/renecannao/proxysql) - High performance proxy for MySQL.
- [MySQL Router](https://dev.mysql.com/doc/mysql-router/en/) - MySQL Router is part of InnoDB cluster, and is a lightweight middleware that provides transparent routing between your application and back-end MySQL Servers.

## Replication

*Replication related software*



## Schema

*Add-on schemas*

- [common_schema](https://github.com/shlomi-noach/common_schema) - DBA's framework for MySQL, providing a function library, views library and QueryScript interpreter.
- [sys](https://github.com/mysql/mysql-sys) - A collection of views, functions and procedures to help MySQL administrators get insight in to MySQL Database usage.


## Security

*Tools that prevents leaking of sensitive data from database (encryption, masking and tokenization, honey-pots, etc)*

- [Acra](https://github.com/cossacklabs/acra) - SQL database protection suite: strong selective encryption, SQL injections prevention, intrusion detection system.

## Server

*MySQL server flavors*

- [MariaDB](https://github.com/MariaDB/server) - Community developed fork of MySQL server.
- [MySQL Server & MySQL Cluster](https://github.com/mysql/mysql-server) - Official Oracle's MySQL server & MySQL Cluster distribution.
- [Percona Server](https://launchpad.net/percona-server) - An enhanced, drop-in MySQL replacement.
- [TiDB](https://github.com/pingcap/tidb) - A distributed HTAP database compatible with the MySQL protocol.

## Sharding

*Sharding solutions/frameworks*

- [jetpants](https://github.com/tumblr/jetpants) - An automation suite for managing large range sharding clusters, by Tumblr.
- [vitess](https://github.com/vitessio/vitess) - vitess provides servers and tools which facilitate scaling of MySQL databases for large scale web services.


## Toolkits

*Toolkits, general purpose scripts*

- [gh-ost](https://github.com/github/gh-ost/) - GitHub's online schema migration for MySQL.
- [go-mysql](https://github.com/siddontang/go-mysql) - A pure go library to handle MySQL network protocol and replication.
- [MySQL Utilities](https://dev.mysql.com/downloads/utilities/) - a collection of command-line utilities, written in Python, that are used for maintaining and administering MySQL servers, either individually, or within Replication hierarchies.
- [openark kit](http://code.openark.org/forge/openark-kit) - a set of utilities that solve everyday maintenance tasks, which may be complicated or time consuming to do by hand, written in Python.
- [Percona Toolkit](https://www.percona.com/software/mysql-tools/percona-toolkit) - a collection of advanced command-line tools to perform a variety of MySQL server and system tasks that are too difficult or complex to perform manually.
- [UnDROP](https://bitbucket.org/Marc-T/undrop-for-innodb) - a tool to recover data from dropped or corrupted InnoDB tables.

# Resources

*At this stage "resources" will not include websites, blogs, slides, presentation videos, etc. in fear of list size*

## Conferences

*Public, recurring conferences on and around MySQL*

- [FOSDEM](https://fosdem.org/) - a free event for software developers to meet, share ideas and collaborate. Annually, in Brussels. Offers "MySQL & friends" room.
- [MySQL Central](https://www.oracle.com/openworld/mysql/index.html) - Oracle's annual MySQL conference, as part of Oracle Open World.
- [Percona Live](https://www.percona.com/live/conferences) - MySQL & Openstack focused conference.
- [SCALE](https://www.socallinuxexpo.org) - A community organized Linux and Open Source conference held annually in Southern California. The local MySQL community runs a track under the name MySQL Community Day.

## e-books

*e-books as well as relevant materials on and around MySQL*

- [Database Systems Lecture Notes](http://spots.augusta.edu/caubert/db/ln/) - lecture notes on Database Systems (available in pdf, html, odt and markdown) including a Chapter on SQL that covers basic set-up, exercises and problems.
- [SQL-exercise](https://github.com/XD-DENG/SQL-exercise) - contains several SQL exercises, including the schema description figure, SQL code to build schema, questions and solutions in SQL. Based on wikibook [SQL Exercises](https://en.wikibooks.org/wiki/SQL_Exercises).

## Media

*Public, ongoing video & audio casts. This excludes conference presentations in fear of list size*


## Newsletters

*Newsletters require an email address, by definition. List below are newsletters that require nothing but an email address*
