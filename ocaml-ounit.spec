%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Unit test framework for OCaml
Name:		ocaml-ounit
Version:	2.0.0
Release:	2
License:	MIT
Group:		Development/Other
Url:		https://ounit.forge.ocamlcore.org/
Source0:	http://download.ocamlcore.org/ounit/ounit/%{version}/ounit-%{version}.tar.gz
Source1:	http://download.ocamlcore.org/ounit/ounit/%{version}/ounit-doc-%{version}.tar.gz
BuildRequires:	camlp4
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib
BuildRequires:	libxml2-utils

%description
OUnit is a unit test framework for OCaml. It allows one to easily
create unit-tests for OCaml code. It is based on HUnit, a unit testing
framework for Haskell. It is similar to JUnit, and other xUnit testing
frameworks.

%files
%doc LICENSE.txt README.txt AUTHORS.txt
%dir %{_libdir}/ocaml/oUnit
%{_libdir}/ocaml/oUnit/*.cmi
%{_libdir}/ocaml/oUnit/*.cma
%{_libdir}/ocaml/oUnit/*.cmxs
%{_libdir}/ocaml/oUnit/META

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%files devel
%doc doc/
%doc examples/ test/
%doc api-doc-html/
%doc api-ounit/
%{_libdir}/ocaml/oUnit/*.a
%{_libdir}/ocaml/oUnit/*.cmxa
%{_libdir}/ocaml/oUnit/*.cmx
%{_libdir}/ocaml/oUnit/*.mli
%{_libdir}/ocaml/oUnit/*.ml

#----------------------------------------------------------------------------

%prep
%setup -q -n ounit-%{version}

%build
ocaml setup.ml -configure --enable-tests
ocaml setup.ml -build
ocaml setup.ml -doc

mv _build/src/api-ounit.docdir api-doc-html

tar xzf %{SOURCE1}
mv ounit-doc-%{version}/api-ounit/ .

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
ocaml setup.ml -install

%check
ocaml setup.ml -test

