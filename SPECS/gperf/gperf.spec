Summary:	Gperf-3.0.4
Name:		gperf
Version:	3.0.4
Release:	1%{?dist}
License:	GPLv3+
URL:		http://freedesktop.org/wiki/Software/%{name}l/
Source0:	http://ftp.gnu.org/gnu/gperf/%{name}-%{version}.tar.gz
Group:		Development/Tools
Vendor:		VMware, Inc.
Distribution: 	Photon
%description
Gperf generates a perfect hash function from a key set.
%prep
%setup -q
%build
./configure \
	--prefix=%{_prefix} \
	--docdir=%{_defaultdocdir}/%{name}-%{version}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
install -v -m644 doc/gperf.{dvi,ps,pdf} %{buildroot}/%{_docdir}/%{name}-%{version}
pushd  %{buildroot}/usr/share/info &&
  for FILENAME in *; do
    install-info $FILENAME %{name}-%{version} 2>/dev/null
  done &&
popd
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%files
%defattr(-,root,root)
%{_docdir}/%{name}-%{version}/*
%{_mandir}/man1/*
%{_datadir}/info/*
%{_bindir}/*
%changelog
*	Thu Oct 23 2014 Divya Thaluru <dthaluru@vmware.com> 3.0.4-1
-	Initial build. First version
