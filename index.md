---
layout: default
---
A curated list of awesome MySQL software, libraries and resources. [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

This list accepts and encourages pull requests. See [CONTRIBUTING](https://github.com/shlomi-noach/awesome-mysql/blob/master/CONTRIBUTING.md)

### Contents

- [Awesome MySQL](#awesome-mysql)
    - [Analysis](#analysis)
    - [Backup](#backup)
    - [Benchmarking](#benchmarking)
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
- [Prometheus](https://prometheus.io/)/[mysqld_exporter](https://github.com/prometheus/mysqld_exporter) - Time series database for real-time monitoring and alerting.
- [pstop](https://github.com/sjmudd/ps-top) - a top-like program for MySQL, collecting, aggregating and displaying information from performance_schema.
- [mysql-statsd](https://github.com/db-art/mysql-statsd) - A Python daemon to collect information from MySQL and send it via StatsD to Graphite.
- [MySQLTuner-perl](http://mysqltuner.com) - A script that allows you to review a MySQL installation quickly and make adjustments to increase performance and stability.
- [Percona Monitoring and Management](https://www.percona.com/doc/percona-monitoring-and-management/index.html) -  An open-source platform for managing and monitoring MySQL performance. 
## Backup

*Backup/restore/recovery tools*

- [MyDumper](https://launchpad.net/mydumper) - Logical, parallel backup/dumper tool for MySQL
- [MySQLDumper](http://www.mysqldumper.net/) - open-source web based backup tool - useful for shared webhosting
- [Percona Xtrabackup](http://www.percona.com/doc/percona-xtrabackup) - an open-source hot backup utility for MySQL - based servers that doesn’t lock your database during the backup.

## Benchmarking

*Tools to stress your servers*

- [iibench-mysql](https://github.com/tmcallaghan/iibench-mysql) - Java based version of the Index Insertion Benchmark for MySQL/Percona/MariaDB.
- [Sysbench](https://github.com/akopytov/sysbench) - a modular, cross-platform and multi-threaded benchmark tool.
- [TPCC-MySQL](https://code.launchpad.net/~percona-dev/perconatools/tpcc-mysql) - A port of the popular [TPCC](http://www.tpc.org/tpcc/) benchmark for MySQL.

## ChatOps

*Scripts integrated into chat rooms*

- [Hubot MySQL ChatOps](https://github.com/samlambert/hubot-mysql-chatops)

## Configuration

*MySQL sample configuration and advisors*

- [mysql-compatibility-config](https://github.com/morgo/mysql-compatibility-config) - make MySQL configuration behave more like newer (or older) releases of MySQL.

## Connectors

*MySQL connectors for various programming languages*

- [Connector/Python](https://dev.mysql.com/downloads/connector/python/) - a standardized database driver for Python platforms and development.
- [Connector/Net](https://dev.mysql.com/downloads/connector/net/) - a standardized database driver for .Net platforms and development.
- [Connector/J](https://dev.mysql.com/downloads/connector/j/) - a standardized database driver for the Java platforms and development.
- [DBD::mysql](https://metacpan.org/pod/DBD::mysql) - MySQL driver for the Perl5 Database Interface.
- [go-sql-driver](https://github.com/go-sql-driver/mysql) - a lightweight and fast MySQL-Driver for Go's (golang) database/sql package.
- [libAttachSQL](https://github.com/libattachsql/libattachsql) - libAttachSQL is a lightweight, non-blocking C API for MySQL servers.
- [MariaDB Java Client](https://mariadb.com/kb/en/mariadb/mariadb-connector-j/) - LGPL-licensed MariaDB Client Library for Java Applications.
- [mysqlclient-python](https://github.com/PyMySQL/mysqlclient-python) - (Old) MySQL database connector for Python.
- [node-mysql](https://github.com/felixge/node-mysql) - A pure Nodejs Javascript client implementing the MySQL protocol.
- [PHP mysqlnd](https://dev.mysql.com/downloads/connector/php-mysqlnd/) - MySQL native driver for MySQL, deprecating older libmysql based driver.
- [PyMySQL](https://github.com/PyMySQL/PyMySQL) - MySQL database connector for Python.
- [Ruby Mysql2 gem](https://github.com/brianmario/mysql2) - MySQL driver for Ruby and Rails projects.

## Deployment

*MySQL deployment tools*

- [MySQL Docker](https://hub.docker.com/_/mysql/) - Official Docker images.
- [MySQL Sandbox](http://mysqlsandbox.net/) - a tool that installs one or more MySQL servers within seconds, easily, securely, and with full control.


## Development

*Tools to support MySQL-related development*

- [Flywaydb](http://flywaydb.org/getstarted/) - Database migrations; Evolve your database schema easily and reliably across all your instances
- [Liquibase](http://www.liquibase.org/) - Source control for your database
- [Propagator](https://github.com/outbrain/propagator) - Centralized schema & data deployment on a multi-everything topology
- [Shift](https://github.com/square/shift) - An application that helps you run schema migrations on MySQL databases


## GUI

*GUI frontends & applications*

- [Adminer](https://www.adminer.org/) - Database management in a single PHP file.
- [HeidiSQL](http://www.heidisql.com/) - MySQL GUI frontend for Windows.
- [MySQL Workbench](http://dev.mysql.com/downloads/workbench/) - provides DBAs and developers an integrated tools environment for database design & modeling; SQL devleopment; database administration.
- [phpMyAdmin](https://www.phpmyadmin.net/) - a free software tool written in PHP, intended to handle the administration of MySQL over the Web.
- [SequelPro](https://github.com/sequelpro/sequelpro) - a Mac database management application for working with MySQL databases.
- [mycli](https://github.com/dbcli/mycli) - A Terminal Client for MySQL with AutoCompletion and Syntax Highlighting.
- [SQLyog Community edition](https://github.com/webyog/sqlyog-community/wiki/Downloads) - SQLyog Community edition. For Windows, works fine under wine in Mac and Linux
- [Percona Monitoring and Management](https://www.percona.com/doc/percona-monitoring-and-management/index.html) -  An open-source platform for managing and monitoring MySQL performance. 
- [pspg](https://github.com/okbob/pspg) - provides a pager with enhanced visualization and navigation for tabular data. Originally implemented for PostgreSQL, but also supports MySQL.


## HA

*High availability solutions*

- [Galera Cluster](http://galeracluster.com/products/) - a true Multimaster Cluster based on synchronous replication.
- [MariaDB Replication Manager](https://github.com/mariadb-corporation/replication-manager) - a high availability solution to manage MariaDB 10.x GTID replication.
- [MHA](http://code.google.com/p/mysql-master-ha/) - Master High Availability Manager and tools for MySQL
- [MySQL Fabric](https://www.mysql.com/products/enterprise/fabric.html) - an extensible framework for managing farms of MySQL Servers.
- [Percona Replication Manager](https://github.com/percona/percona-pacemaker-agents/) - Asynchronous MySQL replication manager agent for Pacemaker. Supports file and GTID based replication, geo-distributed clusters using booth.


## Proxy

*Proxies to MySQL*

- [MaxScale](https://github.com/mariadb-corporation/MaxScale) - open-source, database-centric proxy.
- [Mixer](https://github.com/siddontang/mixer) - a MySQL proxy powered by Go which aims to supply a simple solution for MySQL sharding.
- [MySQL Proxy](https://launchpad.net/mysql-proxy) - A simple program that sits between your client and MySQL server(s) that can monitor, analyze or transform their communication.
- [ProxySQL](https://github.com/renecannao/proxysql) - High performance proxy for MySQL.
- [MySQL Router](https://dev.mysql.com/doc/mysql-router/en/) - MySQL Router is lightweight middleware that provides transparent routing between your application and any backend MySQL Servers.

## Replication

*Replication related software*

- [orchestrator](https://github.com/outbrain/orchestrator) - MySQL replication topology management and visualization tool.
- [Tungsten Replicator](https://github.com/vmware/tungsten-replicator) - A high performance, open source, data replication engine for MySQL.


## Schema

*Add-on schemas*

- [common_schema](https://github.com/shlomi-noach/common_schema) - DBA's framework for MySQL, providing a function library, views library and QueryScript interpreter.
- [sys](https://github.com/mysql/mysql-sys) - A collection of views, functions and procedures to help MySQL administrators get insight in to MySQL Database usage.


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

- [go-mysql](https://github.com/siddontang/go-mysql) - A pure go library to handle MySQL network protocol and replication.
- [MySQL Utilities](https://dev.mysql.com/downloads/utilities/) - a collection of command-line utilities, written in Python, that are used for maintaining and administering MySQL servers, either individually, or within Replication hierarchies.
- [Percona Toolkit](https://www.percona.com/software/mysql-tools/percona-toolkit) - a collection of advanced command-line tools to perform a variety of MySQL server and system tasks that are too difficult or complex to perform manually.
- [gh-ost](https://github.com/github/gh-ost/) - GitHub's online schema migration for MySQL.
- [openark kit](http://code.openark.org/forge/openark-kit) - a set of utilities that solve everyday maintenance tasks, which may be complicated or time consuming to do by hand, written in Python.
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

- [SQL-exercise](https://github.com/XD-DENG/SQL-exercise) - contains several SQL exercises, including the schema description figure, SQL code to build schema, questions and solutions in SQL. Based on wikibook [SQL Exercises](https://en.wikibooks.org/wiki/SQL_Exercises).

## Media

*Public, ongoing video & audio casts. This excludes conference presentations in fear of list size*

- [DBHangOps](http://dbhangops.github.io/) - a bi-weekly google hangout meeting of various members of the MySQL community that simply want to talk shop about MySQL in their day-to-day .
- [OurSQL Podcast](http://www.oursql.com/) - The MySQL database community podcast.


## Newsletters

*Newsletters require an email address, by definition. List below are newsletters that require nothing but an email address*

- [Weekly MySQL News](http://mysqlnewsletter.com/) - Unofficial weekly news digest of all things MySQL.
