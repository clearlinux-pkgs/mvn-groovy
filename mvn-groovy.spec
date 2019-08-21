#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-groovy
Version  : 2.4.12
Release  : 2
URL      : https://github.com/apache/groovy/archive/GROOVY_2_4_12.tar.gz
Source0  : https://github.com/apache/groovy/archive/GROOVY_2_4_12.tar.gz
Source1  : https://repo.gradle.org/gradle/libs-releases/org/codehaus/groovy/groovy-all/2.4.12/groovy-all-2.4.12.jar
Source2  : https://repo.gradle.org/gradle/libs-releases/org/codehaus/groovy/groovy-all/2.4.12/groovy-all-2.4.12.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : ANTLR-PD Apache-2.0 BSD-3-Clause BSD-3-Clause-Clear EPL-1.0 MIT Public-Domain
Requires: mvn-groovy-data = %{version}-%{release}
Requires: mvn-groovy-license = %{version}-%{release}
BuildRequires : apache-ant
BuildRequires : buildreq-mvn
BuildRequires : gradle

%description
//////////////////////////////////////////
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

%package data
Summary: data components for the mvn-groovy package.
Group: Data

%description data
data components for the mvn-groovy package.


%package license
Summary: license components for the mvn-groovy package.
Group: Default

%description license
license components for the mvn-groovy package.


%prep
%setup -q -n groovy-GROOVY_2_4_12

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-groovy
cp benchmark/bench/LICENSE %{buildroot}/usr/share/package-licenses/mvn-groovy/benchmark_bench_LICENSE
cp licenses/LICENSE-ALLJARJAR %{buildroot}/usr/share/package-licenses/mvn-groovy/licenses_LICENSE-ALLJARJAR
cp licenses/LICENSE-BASE %{buildroot}/usr/share/package-licenses/mvn-groovy/licenses_LICENSE-BASE
cp licenses/LICENSE-BINZIP %{buildroot}/usr/share/package-licenses/mvn-groovy/licenses_LICENSE-BINZIP
cp licenses/LICENSE-DOC %{buildroot}/usr/share/package-licenses/mvn-groovy/licenses_LICENSE-DOC
cp licenses/LICENSE-JARJAR %{buildroot}/usr/share/package-licenses/mvn-groovy/licenses_LICENSE-JARJAR
cp licenses/antlr2-license.txt %{buildroot}/usr/share/package-licenses/mvn-groovy/licenses_antlr2-license.txt
cp licenses/asciidoc-style-license.txt %{buildroot}/usr/share/package-licenses/mvn-groovy/licenses_asciidoc-style-license.txt
cp licenses/asm-license.txt %{buildroot}/usr/share/package-licenses/mvn-groovy/licenses_asm-license.txt
cp licenses/hamcrest-license.txt %{buildroot}/usr/share/package-licenses/mvn-groovy/licenses_hamcrest-license.txt
cp licenses/jline2-license.txt %{buildroot}/usr/share/package-licenses/mvn-groovy/licenses_jline2-license.txt
cp licenses/jquery-js-license.txt %{buildroot}/usr/share/package-licenses/mvn-groovy/licenses_jquery-js-license.txt
cp licenses/jsr166y-license.txt %{buildroot}/usr/share/package-licenses/mvn-groovy/licenses_jsr166y-license.txt
cp licenses/jsr223-license.txt %{buildroot}/usr/share/package-licenses/mvn-groovy/licenses_jsr223-license.txt
cp licenses/junit-license.txt %{buildroot}/usr/share/package-licenses/mvn-groovy/licenses_junit-license.txt
cp licenses/normalize-stylesheet-license.txt %{buildroot}/usr/share/package-licenses/mvn-groovy/licenses_normalize-stylesheet-license.txt
cp licenses/xstream-license.txt %{buildroot}/usr/share/package-licenses/mvn-groovy/licenses_xstream-license.txt
cp src/spec/doc/license.adoc %{buildroot}/usr/share/package-licenses/mvn-groovy/src_spec_doc_license.adoc
cp subprojects/groovy-groovysh/LICENSE %{buildroot}/usr/share/package-licenses/mvn-groovy/subprojects_groovy-groovysh_LICENSE
cp subprojects/groovy-jsr223/LICENSE %{buildroot}/usr/share/package-licenses/mvn-groovy/subprojects_groovy-jsr223_LICENSE
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.4.12
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.4.12/groovy-all-2.4.12.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.4.12
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.4.12/groovy-all-2.4.12.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.4.12/groovy-all-2.4.12.jar
/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.4.12/groovy-all-2.4.12.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-groovy/benchmark_bench_LICENSE
/usr/share/package-licenses/mvn-groovy/licenses_LICENSE-ALLJARJAR
/usr/share/package-licenses/mvn-groovy/licenses_LICENSE-BASE
/usr/share/package-licenses/mvn-groovy/licenses_LICENSE-BINZIP
/usr/share/package-licenses/mvn-groovy/licenses_LICENSE-DOC
/usr/share/package-licenses/mvn-groovy/licenses_LICENSE-JARJAR
/usr/share/package-licenses/mvn-groovy/licenses_antlr2-license.txt
/usr/share/package-licenses/mvn-groovy/licenses_asciidoc-style-license.txt
/usr/share/package-licenses/mvn-groovy/licenses_asm-license.txt
/usr/share/package-licenses/mvn-groovy/licenses_hamcrest-license.txt
/usr/share/package-licenses/mvn-groovy/licenses_jline2-license.txt
/usr/share/package-licenses/mvn-groovy/licenses_jquery-js-license.txt
/usr/share/package-licenses/mvn-groovy/licenses_jsr166y-license.txt
/usr/share/package-licenses/mvn-groovy/licenses_jsr223-license.txt
/usr/share/package-licenses/mvn-groovy/licenses_junit-license.txt
/usr/share/package-licenses/mvn-groovy/licenses_normalize-stylesheet-license.txt
/usr/share/package-licenses/mvn-groovy/licenses_xstream-license.txt
/usr/share/package-licenses/mvn-groovy/src_spec_doc_license.adoc
/usr/share/package-licenses/mvn-groovy/subprojects_groovy-groovysh_LICENSE
/usr/share/package-licenses/mvn-groovy/subprojects_groovy-jsr223_LICENSE
