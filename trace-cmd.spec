%define name trace-cmd
%define version 1.0.4
%define release %mkrel 2
%define hash 0d25222

Summary: User interface to Ftrace
Name: %{name}
Version: %{version}
Release: %{release}
License: GPLv2
Group: Development/Kernel
URL: https://git.kernel.org/?p=linux/kernel/git/rostedt/trace-cmd.git;a=summary
Source0: %{name}-%{hash}.tar.gz
Patch0: remove_locate_use.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: docbook-style-xsl == 1.75.2
BuildRequires: asciidoc

%description
trace-cmd is a user interface to Ftrace. Instead of needing to use the
debugfs directly, trace-cmd will handle of setting of options and
tracers and will record into a data file.

%prep
%setup -q -n %{name}-%{hash}
%patch0 -p1

%build
make DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix} install
export MANPAGE_DOCBOOK_XSL="/usr/share/sgml/docbook/xsl-stylesheets-1.75.2/manpages/docbook.xsl"
make DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix} install_doc

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
%{_bindir}/%{name}
%{_datadir}/%{name}/plugins/*
%{_mandir}/*/*
