%define _tag daos-sampler-%{version}

Name:           ovis-daos-sampler
Version:        1.0.1
Release:        1
Summary:        DAOS sampler for LDMS
License:        GPLv2
Group:          System/Libraries
Url:            https://github.com/ovis-hpc/ovis
Source:         https://github.com/daos-stack/ovis/archive/refs/tags/%{_tag}.tar.gz
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel
BuildRequires:  openssl-devel
BuildRequires:  libevent libevent-devel
BuildRequires:  autoconf >= 2.63
BuildRequires:  gcc make automake libtool bison flex
BuildRequires:  daos-devel >= 2.1.100
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains the DAOS sampler plugin for LDMS. It is intended to be
installed alongside vendor-provided LDMS RPMs which provide the actual
LDMS daemons and tools.

%prep
%autosetup
./autogen.sh

%build
%configure \
  --disable-rpath \
  --disable-scripts \
  --disable-doc-man \
  --disable-mmap \
  --disable-perf \
  --disable-store \
  --disable-flatfile \
  --disable-csv \
  --disable-lustre \
  --disable-clock \
  --disable-synthetic \
  --disable-varset \
  --disable-lnet_stats \
  --disable-meminfo \
  --disable-array_example \
  --disable-hello_stream \
  --disable-blob_stream \
  --disable-procinterrupts \
  --disable-procnet \
  --disable-procnetdev \
  --disable-procnfs \
  --disable-dstat \
  --disable-procstat \
  --disable-llnl-edac \
  --disable-tsampler \
  --disable-cray_power_sampler \
  --disable-loadavg \
  --disable-vmstat \
  --disable-procdiskstats \
  --disable-spaceless_names \
  --disable-generic_sampler \
  --disable-jobinfo-sampler \
  --disable-readline \
  --disable-python \
  --disable-ldms-python

make %{?_smp_mflags}

%check
%{__make} check

%install
%{__make} DESTDIR=%{?buildroot} install-strip -C ldms/src/contrib/sampler/daos
rm -f $RPM_BUILD_ROOT/%{_libdir}/ovis-ldms/libdaos_sampler.{a,la}

%files
%defattr(-,root,root)
%{_libdir}/ovis-ldms/libdaos_sampler.*
%{_mandir}/man7/Plugin_daos_sampler.7.gz

%changelog
* Wed Jul 06 2022 Michael J. MacDonald <mjmac.macdonald@intel.com> - 1.0.1-1
- Add %check step to verify sampler functionality.

* Fri Apr 29 2022 Michael J. MacDonald <mjmac.macdonald@intel.com> - 1.0.0-1
- Restore libdaos_sampler.so (ldmsd wants to see it); disable rpmlint errors.

* Thu Apr 28 2022 Michael J. MacDonald <mjmac.macdonald@intel.com> - 1.0.0-0
- Initial packaging
