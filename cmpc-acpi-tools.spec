Name:	cmpc-acpi-tools
Version:	0.0.1
Release:	1
Summary: ACPI tools for ClassmatePC

Group: System/Kernel and hardware
License: GPLv3+
Source0: %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: acpi

%description
ACPI events and scripts for support ClassmatePC acpi-related parts.

%prep
%setup -q

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/acpi/{actions,events}
install -m 755 actions/* %{buildroot}%{_sysconfdir}/acpi/actions
install -m 755 events/* %{buildroot}%{_sysconfdir}/acpi/events

%clean
rm -rf %{buildroot}


%files
%{_sysconfdir}/acpi/*
