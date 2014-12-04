Name:           capstone
Version:        3.0
Release:        1%{?dist}
Summary:        Multi-arch, multi-platform disassembly engine

License:        BSD
URL:            http://www.capstone-engine.org
Source0:        https://github.com/aquynh/%{name}/archive/master.zip

#Patch1:		00-ocaml-fix.patch

#BuildRequires:  
#Requires:       %{name}-devel

%description
Provides a multi-arch, multi-platform disassembly
 framework with advanced features.

%package	devel
Summary:	Development files for the %{name} package

%description	devel
Development files for the %{name} package. See %{name} package for more
 information.

%package	devel-python
Summary:	Python bindings for the %{name} package
BuildRequires:	python python2-devel

%description	devel-python
Python bindings for the %{name} package. See %{name} package for more
 information.

%package	devel-java
Summary:	Java bindings for the %{name} package
BuildRequires:	jna java-devel

%description	devel-java
Java bindings for the %{name} package. See %{name} package for more
 information.

#%package 	ocaml-binding
#Summary:	OCaml bindings for the %{name} package
#BuildRequires:  ocaml, ocaml-findlib-devel

#%define _use_internal_dependency_generator 0
#%define __find_requires /usr/lib/rpm/ocaml-find-requires.sh
#%define __find_provides /usr/lib/rpm/ocaml-find-provides.sh

#%description	ocaml-binding
#OCaml bindings for the %{name} package. See %{name} package for more information.

%prep
%setup -q -n %{name}-master
#%patch1 -p0

%build
./make.sh default
cd bindings
make
cd python
make
cd ../java
make
#cd ../ocaml
#make

%install
cd bindings/python
python setup.py install --root %{buildroot}
cd ../..
mkdir -p %{buildroot}%{_javadir}
install bindings/java/%{name}.jar %{buildroot}%{_javadir}
#mkdir -p %{buildroot}%{_libdir}/ocaml
#install bindings/ocaml/%{name}.* %{buildroot}%{_libdir}/ocaml
export DESTDIR=%{buildroot}
./make.sh install

%files
%license {LICENSE,LICENSE_LLVM}.TXT
%doc {COMPILE,CREDITS}.TXT README TODO RELEASE_NOTES ChangeLog
%{_libdir}/libcapstone*
%{_libdir}/pkgconfig/capstone.pc

%files	devel
%{_includedir}/*

%files	devel-python
%{python2_sitelib}/%{name}/
%{python2_sitelib}/%{name}-%{version}-py?.?.egg-info

%files	devel-java
%{_javadir}/%{name}.jar

#%files	ocaml-binding
#%{_libdir}/ocaml/

%post -n %{name} -p /sbin/ldconfig
%postun -n %{name} -p /sbin/ldconfig

%changelog
* Mon Dec  1 2014 root
- 
