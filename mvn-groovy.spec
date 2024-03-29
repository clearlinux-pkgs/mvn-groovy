#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-groovy
Version  : 2.4.12
Release  : 9
URL      : https://github.com/apache/groovy/archive/GROOVY_2_4_12.tar.gz
Source0  : https://github.com/apache/groovy/archive/GROOVY_2_4_12.tar.gz
Source1  : https://repo.gradle.org/gradle/libs-releases/org/codehaus/groovy/groovy-all/2.4.12/groovy-all-2.4.12.jar
Source2  : https://repo.gradle.org/gradle/libs-releases/org/codehaus/groovy/groovy-all/2.4.12/groovy-all-2.4.12.pom
Source3  : https://repo.gradle.org/gradle/libs-releases/org/codehaus/groovy/groovy-all/2.4.15/groovy-all-2.4.15.jar
Source4  : https://repo.gradle.org/gradle/libs-releases/org/codehaus/groovy/groovy-all/2.4.15/groovy-all-2.4.15.pom
Source5  : https://repo.gradle.org/gradle/libs-releases/org/codehaus/groovy/groovy-all/2.4.7/groovy-all-2.4.7.jar
Source6  : https://repo.gradle.org/gradle/libs-releases/org/codehaus/groovy/groovy-all/2.4.7/groovy-all-2.4.7.pom
Source7  : https://repo.gradle.org/gradle/libs-releases/org/codehaus/groovy/groovy-all/2.5.4/groovy-all-2.5.4.pom
Source8  : https://repo.gradle.org/gradle/libs-releases/org/codehaus/groovy/groovy-backports-compat23/2.4.15/groovy-backports-compat23-2.4.15.jar
Source9  : https://repo.gradle.org/gradle/libs-releases/org/codehaus/groovy/groovy-backports-compat23/2.4.15/groovy-backports-compat23-2.4.15.pom
Source10  : https://repo.gradle.org/gradle/libs-releases/org/codehaus/groovy/groovy-xml/2.4.7/groovy-xml-2.4.7.jar
Source11  : https://repo.gradle.org/gradle/libs-releases/org/codehaus/groovy/groovy-xml/2.4.7/groovy-xml-2.4.7.pom
Source12  : https://repo.gradle.org/gradle/libs-releases/org/codehaus/groovy/groovy/2.4.15/groovy-2.4.15.jar
Source13  : https://repo.gradle.org/gradle/libs-releases/org/codehaus/groovy/groovy/2.4.15/groovy-2.4.15.pom
Source14  : https://repo.gradle.org/gradle/libs-releases/org/codehaus/groovy/groovy/2.4.7/groovy-2.4.7.jar
Source15  : https://repo.gradle.org/gradle/libs-releases/org/codehaus/groovy/groovy/2.4.7/groovy-2.4.7.pom
Source16  : https://repo.gradle.org/gradle/libs-releases/org/codehaus/groovy/groovy/2.5.4/groovy-2.5.4.jar
Source17  : https://repo.gradle.org/gradle/libs-releases/org/codehaus/groovy/groovy/2.5.4/groovy-2.5.4.pom
Source18  : https://repo.maven.apache.org/maven2/org/codehaus/groovy/groovy/1.8.3/groovy-1.8.3.jar
Source19  : https://repo.maven.apache.org/maven2/org/codehaus/groovy/groovy/1.8.3/groovy-1.8.3.pom
Source20  : https://repo1.maven.org/maven2/org/codehaus/groovy/groovy-all/2.1.5/groovy-all-2.1.5.pom
Source21  : https://repo1.maven.org/maven2/org/codehaus/groovy/groovy-all/2.4.8/groovy-all-2.4.8.jar
Source22  : https://repo1.maven.org/maven2/org/codehaus/groovy/groovy-all/2.4.8/groovy-all-2.4.8.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : ANTLR-PD Apache-2.0 BSD-3-Clause BSD-3-Clause-Clear CC-BY-2.5 EPL-1.0 MIT Public-Domain
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
cp LICENSE %{buildroot}/usr/share/package-licenses/mvn-groovy/LICENSE
cp NOTICE %{buildroot}/usr/share/package-licenses/mvn-groovy/NOTICE
cp benchmark/bench/LICENSE %{buildroot}/usr/share/package-licenses/mvn-groovy/benchmark_bench_LICENSE
cp licenses/LICENSE-ALLJARJAR %{buildroot}/usr/share/package-licenses/mvn-groovy/licenses_LICENSE-ALLJARJAR
cp licenses/LICENSE-BASE %{buildroot}/usr/share/package-licenses/mvn-groovy/licenses_LICENSE-BASE
cp licenses/LICENSE-BINZIP %{buildroot}/usr/share/package-licenses/mvn-groovy/licenses_LICENSE-BINZIP
cp licenses/LICENSE-DOC %{buildroot}/usr/share/package-licenses/mvn-groovy/licenses_LICENSE-DOC
cp licenses/LICENSE-JARJAR %{buildroot}/usr/share/package-licenses/mvn-groovy/licenses_LICENSE-JARJAR
cp licenses/LICENSE-SDK %{buildroot}/usr/share/package-licenses/mvn-groovy/licenses_LICENSE-SDK
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
cp subprojects/groovy-console/NOTICE %{buildroot}/usr/share/package-licenses/mvn-groovy/subprojects_groovy-console_NOTICE
cp subprojects/groovy-docgenerator/LICENSE %{buildroot}/usr/share/package-licenses/mvn-groovy/subprojects_groovy-docgenerator_LICENSE
cp subprojects/groovy-groovydoc/LICENSE %{buildroot}/usr/share/package-licenses/mvn-groovy/subprojects_groovy-groovydoc_LICENSE
cp subprojects/groovy-groovysh/LICENSE %{buildroot}/usr/share/package-licenses/mvn-groovy/subprojects_groovy-groovysh_LICENSE
cp subprojects/groovy-jsr223/LICENSE %{buildroot}/usr/share/package-licenses/mvn-groovy/subprojects_groovy-jsr223_LICENSE
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.4.12
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.4.12/groovy-all-2.4.12.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.4.12
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.4.12/groovy-all-2.4.12.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.4.15
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.4.15/groovy-all-2.4.15.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.4.15
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.4.15/groovy-all-2.4.15.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.4.7
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.4.7/groovy-all-2.4.7.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.4.7
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.4.7/groovy-all-2.4.7.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.5.4
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.5.4/groovy-all-2.5.4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-backports-compat23/2.4.15
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-backports-compat23/2.4.15/groovy-backports-compat23-2.4.15.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-backports-compat23/2.4.15
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-backports-compat23/2.4.15/groovy-backports-compat23-2.4.15.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-xml/2.4.7
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-xml/2.4.7/groovy-xml-2.4.7.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-xml/2.4.7
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-xml/2.4.7/groovy-xml-2.4.7.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy/2.4.15
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy/2.4.15/groovy-2.4.15.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy/2.4.15
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy/2.4.15/groovy-2.4.15.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy/2.4.7
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy/2.4.7/groovy-2.4.7.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy/2.4.7
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy/2.4.7/groovy-2.4.7.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy/2.5.4
cp %{SOURCE16} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy/2.5.4/groovy-2.5.4.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy/2.5.4
cp %{SOURCE17} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy/2.5.4/groovy-2.5.4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy/1.8.3
cp %{SOURCE18} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy/1.8.3/groovy-1.8.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy/1.8.3
cp %{SOURCE19} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy/1.8.3/groovy-1.8.3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.1.5
cp %{SOURCE20} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.1.5/groovy-all-2.1.5.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.4.8
cp %{SOURCE21} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.4.8/groovy-all-2.4.8.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.4.8
cp %{SOURCE22} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.4.8/groovy-all-2.4.8.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.1.5/groovy-all-2.1.5.pom
/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.4.12/groovy-all-2.4.12.jar
/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.4.12/groovy-all-2.4.12.pom
/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.4.15/groovy-all-2.4.15.jar
/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.4.15/groovy-all-2.4.15.pom
/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.4.7/groovy-all-2.4.7.jar
/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.4.7/groovy-all-2.4.7.pom
/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.4.8/groovy-all-2.4.8.jar
/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.4.8/groovy-all-2.4.8.pom
/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-all/2.5.4/groovy-all-2.5.4.pom
/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-backports-compat23/2.4.15/groovy-backports-compat23-2.4.15.jar
/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-backports-compat23/2.4.15/groovy-backports-compat23-2.4.15.pom
/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-xml/2.4.7/groovy-xml-2.4.7.jar
/usr/share/java/.m2/repository/org/codehaus/groovy/groovy-xml/2.4.7/groovy-xml-2.4.7.pom
/usr/share/java/.m2/repository/org/codehaus/groovy/groovy/1.8.3/groovy-1.8.3.jar
/usr/share/java/.m2/repository/org/codehaus/groovy/groovy/1.8.3/groovy-1.8.3.pom
/usr/share/java/.m2/repository/org/codehaus/groovy/groovy/2.4.15/groovy-2.4.15.jar
/usr/share/java/.m2/repository/org/codehaus/groovy/groovy/2.4.15/groovy-2.4.15.pom
/usr/share/java/.m2/repository/org/codehaus/groovy/groovy/2.4.7/groovy-2.4.7.jar
/usr/share/java/.m2/repository/org/codehaus/groovy/groovy/2.4.7/groovy-2.4.7.pom
/usr/share/java/.m2/repository/org/codehaus/groovy/groovy/2.5.4/groovy-2.5.4.jar
/usr/share/java/.m2/repository/org/codehaus/groovy/groovy/2.5.4/groovy-2.5.4.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-groovy/LICENSE
/usr/share/package-licenses/mvn-groovy/NOTICE
/usr/share/package-licenses/mvn-groovy/benchmark_bench_LICENSE
/usr/share/package-licenses/mvn-groovy/licenses_LICENSE-ALLJARJAR
/usr/share/package-licenses/mvn-groovy/licenses_LICENSE-BASE
/usr/share/package-licenses/mvn-groovy/licenses_LICENSE-BINZIP
/usr/share/package-licenses/mvn-groovy/licenses_LICENSE-DOC
/usr/share/package-licenses/mvn-groovy/licenses_LICENSE-JARJAR
/usr/share/package-licenses/mvn-groovy/licenses_LICENSE-SDK
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
/usr/share/package-licenses/mvn-groovy/subprojects_groovy-console_NOTICE
/usr/share/package-licenses/mvn-groovy/subprojects_groovy-docgenerator_LICENSE
/usr/share/package-licenses/mvn-groovy/subprojects_groovy-groovydoc_LICENSE
/usr/share/package-licenses/mvn-groovy/subprojects_groovy-groovysh_LICENSE
/usr/share/package-licenses/mvn-groovy/subprojects_groovy-jsr223_LICENSE
