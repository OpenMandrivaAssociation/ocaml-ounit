%define name	ocaml-ounit
%define version	1.0.3
%define release	5

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    Unit test framework for OCaml
Group:      Development/Other
License:    MIT
URL:        http://www.xs4all.nl/~mmzeeman/ocaml/
Source0:    http://www.xs4all.nl/~mmzeeman/ocaml/ounit-%{version}.tar.gz
BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
OUnit is a unit test framework for OCaml. It allows one to easily
create unit-tests for OCaml code. It is based on HUnit, a unit testing
framework for Haskell. It is similar to JUnit, and other xUnit testing
frameworks.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n ounit-%{version}

%build
make all
make allopt
make doc

%check
make test

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_libdir}/ocaml/stublibs
make install DESTDIR=%{buildroot} OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENCE
%dir %{_libdir}/ocaml/oUnit
%{_libdir}/ocaml/oUnit/*.cmi
%{_libdir}/ocaml/oUnit/*.cma
%{_libdir}/ocaml/oUnit/META

%files devel
%defattr(-,root,root)
%doc LICENCE README doc
%{_libdir}/ocaml/oUnit/*.a
%{_libdir}/ocaml/oUnit/*.cmxa
%{_libdir}/ocaml/oUnit/*.mli



%changelog
* Wed May 09 2012 Crispin Boylan <crisb@mandriva.org> 1.0.3-5
+ Revision: 797735
- Rebuild

* Mon Jan 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.3-4mdv2011.0
+ Revision: 496358
- rebuild

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.3-3mdv2010.0
+ Revision: 389929
- rebuild

* Mon Dec 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.3-2mdv2009.1
+ Revision: 320708
- move non-devel files in main package
- site-lib hierarchy doesn't exist anymore

* Thu Sep 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.3-1mdv2009.0
+ Revision: 280409
- update to new version 1.0.3

* Thu Aug 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.2-1mdv2009.0
+ Revision: 271914
- import ocaml-ounit

