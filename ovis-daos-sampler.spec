%define _tag daos-sampler-%{version}

Name:           ovis-daos-sampler
Version:        1.0.0
Release:        0
Summary:	DAOS sampler for LDMS
License:        GPLv2
Group:          System Environment/Libraries
Url:            https://github.com/ovis-hpc/ovis
Source:         https://github.com/daos-stack/ovis/archive/refs/tags/%{_tag}.tar.gz
BuildRequires:  gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	openssl-devel
BuildRequires:	libevent libevent-devel
BuildRequires:	autoconf >= 2.63
BuildRequires:	gcc make automake libtool bison flex
BuildRequires:	daos-devel >= 2.1.100
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
  --with-daos=/usr \
  --disable-scripts \
  --disable-doc-man \
  --disable-mmap \
  --disable-perf \
  --disable-store \
  --disable-flatfile \
  --disable-csv \
  --disable-sampler \
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

%install
%make_install -C ldms/src/contrib/sampler/daos

%post
%postun

%files
%defattr(-,root,root)
%{_libdir}/ovis-ldms/libdaos.*
%{_mandir}/man7/Plugin_daos.7.gz

%changelog
* Thu Apr 28 2022 Michael J. MacDonald <mjmac.macdonald@intel.com> - 1.0.0-0
- Initial packaging