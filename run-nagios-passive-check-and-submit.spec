%define name run-nagios-passive-check-and-submit
%define version 0.1.3
%define release 1%{?dist}

Summary: Run a Nagios passive check and submit its result via the Nagios CGI
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Mike Gerber <mike@sprachgewalt.de>

BuildRequires: python2-devel
Requires: %{py2_dist beautifulsoup4 lxml requests termcolor}
Requires: python-yaml

%description
Run a Nagios passive check and submit its result via the Nagios CGI.

%prep
%setup -n %{name}-%{version} -n %{name}-%{version}

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
