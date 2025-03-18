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
- [MySQLTuner-perl](https://github.com/major/MySQLTuner-perl) - A script that allows you to review a MySQL installation quickly and make adjustments to increase performance and stability.
- [Prometheus](https://github.com/prometheus/prometheus)/[mysqld_exporter](https://github.com/prometheus/mysqld_exporter) - Time series database for real-time monitoring and alerting.
- [pstop](https://github.com/sjmudd/ps-top) - a top-like program for MySQL, collecting, aggregating and displaying information from performance_schema.
- [Wireshark](https://gitlab.com/wireshark/wireshark/) - a protocol analyzer that can decode the MySQL protocol.
- [Dolphie](https://github.com/charles-001/dolphie) - a modern terminal tool for real-time analytics into MySQL/MariaDB & ProxySQL

## Backup

*Backup/restore/recovery tools*

- [Dumpling](https://github.com/pingcap/tidb/tree/master/dumpling) - Logical, parallel backup/dumper tool for MySQL/TiDB written in GoLang - support csv format output and integrated as library
- [MyDumper](https://github.com/mydumper/mydumper) - Logical, parallel backup/dumper tool for MySQL
- [Percona Xtrabackup](https://github.com/percona/percona-xtrabackup) - an open-source hot backup utility for MySQL - based servers that doesn’t lock your database during the backup.

## Benchmarking

*Tools to stress your servers*

- [go-tpc](https://github.com/pingcap/go-tpc) - A golang port of [TPCC](http://www.tpc.org/tpcc/) and [TPCH](http://www.tpc.org/tpch/) benchmark for MySQL.
- [iibench-mysql](https://github.com/tmcallaghan/iibench-mysql) - Java based version of the Index Insertion Benchmark for MySQL/Percona/MariaDB.
- [Sysbench](https://github.com/akopytov/sysbench) - a modular, cross-platform and multi-threaded benchmark tool.
- [TPCC-MySQL](https://github.com/Percona-Lab/tpcc-mysql) (archived) - A port of the popular [TPCC](http://www.tpc.org/tpcc/) benchmark for MySQL.

## Binlog-Replication

- [DM](https://github.com/pingcap/tiflow) - A High-Availability data migration platform which supports migrating data from MySQL/MariaDB to TiDB and merging shard tables
- [Kingbus](https://github.com/flike/kingbus) - A distributed MySQL binlog storage system built on Raft
- [mysql-ripple](https://github.com/google/mysql-ripple) (archived) - Ripple, a server that can serve as a middleman in MySQL replication

## ChatOps

*Scripts integrated into chat rooms*

- [Hubot MySQL ChatOps](https://github.com/samlambert/hubot-mysql-chatops)

## Configuration

*MySQL sample configuration and advisors*

- [mysql-compatibility-config](https://github.com/morgo/mysql-compatibility-config) - make MySQL configuration behave more like newer (or older) releases of MySQL.

## Connectors

*MySQL connectors for various programming languages*

- [ballerinax/mysql](https://github.com/ballerina-platform/module-ballerinax-mysql) - Official Ballerina connector for MySQL.
- [DBD::MariaDB](https://github.com/perl5-dbi/DBD-MariaDB) - MariaDB and MySQL driver for the Perl5 Database Interface.
- [DBD::mysql](https://github.com/perl5-dbi/DBD-mysql) - MySQL driver for the Perl5 Database Interface.
- [go-sql-driver](https://github.com/go-sql-driver/mysql) - a lightweight and fast MySQL-Driver for Go's (golang) database/sql package.
- [libAttachSQL](https://github.com/libattachsql/libattachsql) - libAttachSQL is a lightweight, non-blocking C API for MySQL servers.
- [MariaDB Connector/J](https://github.com/mariadb-corporation/mariadb-connector-j) - LGPL-licensed MariaDB Client Library for Java Applications.
- [mex-mariadb](https://github.com/markuman/mex-mariadb) - MIT licensed MariaDB/MySQL Client Library for GNU Octave and Matlab.
- [MySQL C API](https://dev.mysql.com/downloads/c-api/) - Official C driver for MySQL.
- [MySQL Connector/C++](https://github.com/mysql/mysql-connector-cpp) - Official C/C++ driver for MySQL.
- [MySQL Connector/J](https://github.com/mysql/mysql-connector-j) - a standardized database driver for the Java platforms and development.
- [MySQL Connector/NET](https://github.com/mysql/mysql-connector-net) - a standardized database driver for .Net platforms and development.
- [MySQL Connector/Node.js](https://github.com/mysql/mysql-connector-nodejs) - Official Node.js driver for MySQL.
- [MySQL Connector/Python](https://github.com/mysql/mysql-connector-python) - a standardized database driver for Python platforms and development.
- [mysqlclient-python](https://github.com/PyMySQL/mysqlclient) - MySQL database connector for Python.
- [node-mysql](https://github.com/mysqljs/node) - A pure Nodejs Javascript client implementing the MySQL protocol.
- [PHP mysqlnd](https://www.php.net/manual/en/book.mysqlnd.php) - MySQL native driver for PHP.
- [PyMySQL](https://github.com/PyMySQL/PyMySQL) - MySQL database connector for Python.
- [Ruby Mysql2 gem](https://github.com/brianmario/mysql2) - MySQL driver for Ruby and Rails projects.
- [MyZql](https://github.com/speed2exe/myzql) - MySQL and MariaDB driver in native Zig.
- [wtx](https://github.com/c410-f3r/wtx) - Client for MySQL/MariaDB/Percona written in Rust

## Deployment

*MySQL deployment tools*

- [dbdeployer](https://github.com/datacharmer/dbdeployer) (archived) - A tool that installs one or more MySQL servers within seconds, easily, securely, and with full control.
- [MariaDB4j](https://github.com/MariaDB4j/MariaDB4j) - A Java launcher to run MariaDB without installation or external dependencies.
- [MySQL Docker](https://hub.docker.com/_/mysql/) - Official Docker images.


## Development

*Tools to support MySQL-related development*

- [Flywaydb](https://github.com/flyway/flyway) - Database migrations; Evolve your database schema easily and reliably across all your instances
- [Liquibase](https://github.com/liquibase/liquibase) - Source control for your database
- [Shift](https://github.com/square/shift) - An application that helps you run schema migrations on MySQL databases
- [Skeema](https://github.com/skeema/skeema) - Declarative pure-SQL schema management system for MySQL and MariaDB, with support for sharding and external online schema change tools
- [SQLE](https://github.com/actiontech/sqle/blob/main/README_en.md) - SQLE is a SQL audit platform for DBA or developer
- [Test database](https://github.com/datacharmer/test_db) - A sample MySQL database with an integrated test suite, used to test applications and servers

## GUI

*GUI frontends & applications*

- [Adminer](https://github.com/vrana/adminer/) - Database management in a single PHP file.
- [DBeaver](https://github.com/dbeaver/dbeaver/) - A cross-platform SQL and NoSQL database client.
- [HeidiSQL](https://github.com/HeidiSQL/HeidiSQL) - MySQL GUI frontend for Windows.
- [ILLA Cloud](https://github.com/illacloud/illa-builder) - Low-code internal tool builder integrated with Mysql, can be used as GUI for Mysql. 
- [mycli](https://github.com/dbcli/mycli) - A Terminal Client for MySQL with AutoCompletion and Syntax Highlighting.
- [MySQL Shell](https://github.com/mysql/mysql-shell/) - Advanced client and code editor for MySQL that supports development and administration for the MySQL Server and MySQL InnoDB cluster (AdminAPI) with an interactive JavaScript, Python, or SQL interface.
- [MySQL Workbench](https://github.com/mysql/mysql-workbench) - provides DBAs and developers an integrated tools environment for database design & modeling; SQL devleopment; database administration.
- [Ocelot GUI](https://github.com/ocelot-inc/ocelotgui) - GUI client for MySQL or MariaDB, including debugger.
- [OmniDB: Web tool for database management](https://github.com/OmniDB/OmniDB)
- [Percona Monitoring and Management](https://github.com/percona/pmm) - An open-source platform for managing and monitoring MySQL performance.
- [phpMyAdmin](https://github.com/phpmyadmin/phpmyadmin) - a free software tool written in PHP, intended to handle the administration of MySQL over the Web.
- [pspg](https://github.com/okbob/pspg) - provides a pager with enhanced visualization and navigation for tabular data. Originally implemented for PostgreSQL, but also supports MySQL.
- [Sequel Ace](https://github.com/Sequel-Ace/Sequel-Ace) - a Mac database management application for working with MySQL databases.
- [SQLyog Community edition](https://github.com/webyog/sqlyog-community) - SQLyog Community edition. For Windows, works fine under wine in Mac and Linux
- [WebDB](https://github.com/WebDB-App/app) – Open Source and Efficient Database IDE. Featuring Easy server connection, Modern ERD, Intelligent data generator, AI assistant, NoSQL structure manager, Time machine and Powerful query editor

## HA

*High availability solutions*

- [Galera Cluster](https://github.com/codership/galera) - a true Multimaster Cluster based on synchronous replication.
- [mha4mysql-node](https://github.com/yoshinorim/mha4mysql-node) and [mha4mysql-manager](https://github.com/yoshinorim/mha4mysql-manager) (both unmaintained) - Master High Availability Manager and tools for MySQL.
- [Orchestrator](https://github.com/openark/orchestrator) - MySQL replication topology management and High Availability solution.
- [Percona Replication Manager](https://github.com/percona/replication-manager) - Asynchronous MySQL replication manager agent for Pacemaker. Supports file and GTID based replication, geo-distributed clusters using booth.
- [replication-manager](https://github.com/signal18/replication-manager) - a high availability solution to manage MariaDB 10.x and MySQL & Percona Server 5.7 GTID replication topologies.

## Proxy

*Proxies to MySQL*

- [MySQL Proxy](https://github.com/mysql/mysql-proxy) (deprecated) - A simple program that sits between your client and MySQL server(s) that can monitor, analyze or transform their communication.
- [MySQL Router](https://dev.mysql.com/doc/mysql-router/en/) - MySQL Router is part of InnoDB cluster, and is a lightweight middleware that provides transparent routing between your application and back-end MySQL Servers.
- [ProxySQL](https://github.com/sysown/proxysql) - High performance proxy for MySQL.

## Replication

*Replication related software*

* [data-diff](https://github.com/datafold/data-diff) - Command-line tool and Python library to efficiently diff rows across two different databases.


## Schema

*Add-on schemas*

- [common_schema](https://github.com/shlomi-noach/common_schema) - DBA's framework for MySQL, providing a function library, views library and QueryScript interpreter.
- [sys](https://github.com/mysql/mysql-sys) - A collection of views, functions and procedures to help MySQL administrators get insight in to MySQL Database usage.


## Security

*Tools that prevents leaking of sensitive data from database (encryption, masking and tokenization, honey-pots, etc)*

- [Acra](https://github.com/cossacklabs/acra) - SQL database protection suite: strong selective encryption, SQL injections prevention, intrusion detection system.
- [myldapsync](https://github.com/6eh01der/myldapsync) - Synchronize MySQL or MariaDB users with users in an LDAP directory.

## Server

*MySQL server flavors*

- [MariaDB](https://github.com/MariaDB/server) - Community developed fork of MySQL server.
- [MySQL Server & MySQL Cluster](https://github.com/mysql/mysql-server) - Official Oracle's MySQL server & MySQL Cluster distribution.
- [Percona Server](https://github.com/percona/percona-server) - An enhanced, drop-in MySQL replacement.
- [TiDB](https://github.com/pingcap/tidb) - A distributed HTAP database compatible with the MySQL protocol.

## Sharding

*Sharding solutions/frameworks*

- [Jetpants](https://github.com/tumblr/jetpants) - An automation suite for managing large range sharding clusters, by Tumblr.
- [Vitess](https://github.com/vitessio/vitess) - vitess provides servers and tools which facilitate scaling of MySQL databases for large scale web services.


## Toolkits

*Toolkits, general purpose scripts*

- [gh-ost](https://github.com/github/gh-ost/) - GitHub's online schema migration for MySQL.
- [go-mysql](https://github.com/go-mysql-org/go-mysql) - A pure go library to handle MySQL network protocol and replication.
- [MySQL Utilities](https://github.com/mysql/mysql-utilities) (deprecated) - a collection of command-line utilities, written in Python, that are used for maintaining and administering MySQL servers, either individually, or within Replication hierarchies.
- [Percona Toolkit](https://github.com/percona/percona-toolkit) - a collection of advanced command-line tools to perform a variety of MySQL server and system tasks that are too difficult or complex to perform manually.
- [UnDROP](https://github.com/twindb/undrop-for-innodb) - a tool to recover data from dropped or corrupted InnoDB tables.

# Resources

*At this stage "resources" will not include websites, blogs, slides, presentation videos, etc. in fear of list size*

## e-books

*e-books as well as relevant materials on and around MySQL*

- [Database Systems Lecture Notes](http://spots.augusta.edu/caubert/db/ln/) - lecture notes on Database Systems (available in pdf, html, odt and markdown) including a Chapter on SQL that covers basic set-up, exercises and problems.
- [SQL-exercise](https://github.com/XD-DENG/SQL-exercise) - contains several SQL exercises, including the schema description figure, SQL code to build schema, questions and solutions in SQL. Based on wikibook [SQL Exercises](https://en.wikibooks.org/wiki/SQL_Exercises).

## Media

*Public, ongoing video & audio casts. This excludes conference presentations in fear of list size*

## Newsletters

*Newsletters require an email address, by definition. List below are newsletters that require nothing but an email address*
