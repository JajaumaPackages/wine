%ifarch x86_64
%global lib32dir %{_prefix}/lib
%endif

# The features are enabled by default. Run rpmbuild with '--without <feature>'
# command line switch(es) to disable them selectively. Otherwise, one might
# change 'bcond_without' to 'bcond_with' to invert the defaults.
%bcond_without staging
%bcond_without mpg123
%bcond_without opencl
%bcond_without openal

Name:           wine
Epoch:          2
Version:        2.11
Release:        1%{?dist}
Summary:        A compatibility layer for windows applications

License:        LGPLv2.1+
URL:            http://www.winehq.org
Source0:        http://dl.winehq.org/wine/source/2.x/wine-%{version}.tar.xz
%if %{with staging}
Source1:        https://github.com/wine-compholio/wine-staging/archive/v%{version}.tar.gz
%endif

ExclusiveArch:  %{ix86} x86_64

BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gettext

BuildRequires:  alsa-lib-devel%{?_isa}
BuildRequires:  cairo-devel%{?_isa}
BuildRequires:  cups-devel%{?_isa}
BuildRequires:  dbus-devel%{?_isa}
BuildRequires:  fontconfig-devel%{?_isa}
BuildRequires:  freetype-devel%{?_isa}
BuildRequires:  glib2-devel%{?_isa}
BuildRequires:  gnutls-devel%{?_isa}
BuildRequires:  gsm-devel%{?_isa}
BuildRequires:  gstreamer1-devel%{?_isa}
BuildRequires:  gstreamer1-plugins-base-devel%{?_isa}
BuildRequires:  isdn4k-utils-devel%{?_isa}
BuildRequires:  lcms2-devel%{?_isa}
BuildRequires:  libX11-devel%{?_isa}
BuildRequires:  libXcomposite-devel%{?_isa}
BuildRequires:  libXcursor-devel%{?_isa}
BuildRequires:  libXext-devel%{?_isa}
BuildRequires:  libXfixes-devel%{?_isa}
BuildRequires:  libXi-devel%{?_isa}
BuildRequires:  libXinerama-devel%{?_isa}
BuildRequires:  libXrandr-devel%{?_isa}
BuildRequires:  libXrender-devel%{?_isa}
BuildRequires:  libXxf86vm-devel%{?_isa}
BuildRequires:  libexif-devel%{?_isa}
BuildRequires:  libgphoto2-devel%{?_isa}
BuildRequires:  libjpeg-turbo-devel%{?_isa}
BuildRequires:  libpcap-devel%{?_isa}
BuildRequires:  libpng-devel%{?_isa}
BuildRequires:  libtiff-devel%{?_isa}
BuildRequires:  libv4l-devel%{?_isa}
BuildRequires:  libxml2-devel%{?_isa}
BuildRequires:  libxslt-devel%{?_isa}
BuildRequires:  mesa-libGL-devel%{?_isa}
BuildRequires:  mesa-libGLU-devel%{?_isa}
BuildRequires:  mesa-libOSMesa-devel%{?_isa}
BuildRequires:  ncurses-devel%{?_isa}
BuildRequires:  openldap-devel%{?_isa}
BuildRequires:  pulseaudio-libs-devel%{?_isa}
BuildRequires:  sane-backends-devel%{?_isa}
BuildRequires:  systemd-devel%{?_isa}

%if %{with staging}
BuildRequires:  gtk3-devel%{?_isa}
BuildRequires:  libva-devel%{?_isa}
%endif

%if %{with mpg123}
BuildRequires:  mpg123-devel%{?_isa}
%endif

%if %{with opencl}
BuildRequires:  ocl-icd-devel%{?_isa}
BuildRequires:  opencl-headers
%endif

%if %{with openal}
BuildRequires:  openal-soft-devel%{?_isa}
%endif

%ifarch x86_64
BuildRequires:  alsa-lib-devel(x86-32)
BuildRequires:  cairo-devel(x86-32)
BuildRequires:  cups-devel(x86-32)
BuildRequires:  dbus-devel(x86-32)
BuildRequires:  fontconfig-devel(x86-32)
BuildRequires:  freetype-devel(x86-32)
BuildRequires:  glib2-devel(x86-32)
BuildRequires:  glibc-devel(x86-32)
BuildRequires:  gnutls-devel(x86-32)
BuildRequires:  gsm-devel(x86-32)
BuildRequires:  gstreamer1-devel(x86-32)
BuildRequires:  gstreamer1-plugins-base-devel(x86-32)
BuildRequires:  isdn4k-utils-devel(x86-32)
BuildRequires:  lcms2-devel(x86-32)
BuildRequires:  libX11-devel(x86-32)
BuildRequires:  libXcomposite-devel(x86-32)
BuildRequires:  libXcursor-devel(x86-32)
BuildRequires:  libXext-devel(x86-32)
BuildRequires:  libXfixes-devel(x86-32)
BuildRequires:  libXi-devel(x86-32)
BuildRequires:  libXinerama-devel(x86-32)
BuildRequires:  libXrandr-devel(x86-32)
BuildRequires:  libXrender-devel(x86-32)
BuildRequires:  libXxf86vm-devel(x86-32)
BuildRequires:  libexif-devel(x86-32)
BuildRequires:  libgphoto2-devel(x86-32)
BuildRequires:  libjpeg-turbo-devel(x86-32)
BuildRequires:  libpcap-devel(x86-32)
BuildRequires:  libpng-devel(x86-32)
BuildRequires:  libtiff-devel(x86-32)
BuildRequires:  libv4l-devel(x86-32)
BuildRequires:  libxml2-devel(x86-32)
BuildRequires:  libxslt-devel(x86-32)
BuildRequires:  mesa-libGL-devel(x86-32)
BuildRequires:  mesa-libGLU-devel(x86-32)
BuildRequires:  mesa-libOSMesa-devel(x86-32)
BuildRequires:  ncurses-devel(x86-32)
BuildRequires:  openldap-devel(x86-32)
BuildRequires:  pulseaudio-libs-devel(x86-32)
BuildRequires:  sane-backends-devel(x86-32)
BuildRequires:  systemd-devel(x86-32)

%if %{with staging}
BuildRequires:  gtk3-devel(x86-32)
BuildRequires:  libva-devel(x86-32)
%endif

%if %{with mpg123}
BuildRequires:  mpg123-devel(x86-32)
%endif

%if %{with opencl}
BuildRequires:  ocl-icd-devel(x86-32)
%endif

%if %{with openal}
BuildRequires:  openal-soft-devel(x86-32)
%endif
%endif

%description
Wine as a compatibility layer for UNIX to run Windows applications. This
package includes a program loader, which allows unmodified Windows 3.x/9x/NT
binaries to run on x86 and x86_64 Unixes. Wine can use native system .dll files
if they are available.


%package devel
Summary:        Wine development environment
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
Header, include files and library definition files for developing applications
with the Wine libraries.


%prep
%setup -q

%if %{with staging}
tar -xf %{SOURCE1} --strip-components=1
make -C patches DESTDIR="$(pwd)" install
%endif


%build
%ifarch x86_64
mkdir wine{32,64}-build

# Export some of distribution factory compiler flags manually. Try not to
# export any machine flags (e.g. -m64) as those would break side-by-side WoW64
# building. Exporting -D_FORTIFY_SOURCE=2 issues some (non-fatal) complaints as
# well so let's better hide it from the build system.
export CFLAGS="$(echo %{__global_cflags} | sed -e 's/-Wp,-D_FORTIFY_SOURCE=2//')"
export LDFLAGS="%{__global_ldflags}"

pushd wine64-build
../configure \
    --enable-win64 \
    %{?_without_mpg123} \
    %{?_without_opencl} \
    %{?_without_openal} \
    --program-prefix=%{?_program_prefix} \
    --prefix=%{_prefix} \
    --exec-prefix=%{_exec_prefix} \
    --bindir=%{_bindir} \
    --sbindir=%{_sbindir} \
    --sysconfdir=%{_sysconfdir} \
    --datadir=%{_datadir} \
    --includedir=%{_includedir} \
    --libdir=%{_libdir} \
    --libexecdir=%{_libexecdir} \
    --localstatedir=%{_localstatedir} \
    --sharedstatedir=%{_sharedstatedir} \
    --mandir=%{_mandir} \
    --infodir=%{_infodir}
make %{?_smp_mflags}
popd

pushd wine32-build
PKG_CONFIG_PATH=%{lib32dir}/pkgconfig/ ../configure \
    --with-wine64=../wine64-build/ \
    %{?_without_mpg123} \
    %{?_without_opencl} \
    %{?_without_openal} \
    --program-prefix=%{?_program_prefix} \
    --prefix=%{_prefix} \
    --exec-prefix=%{_exec_prefix} \
    --bindir=%{_bindir} \
    --sbindir=%{_sbindir} \
    --sysconfdir=%{_sysconfdir} \
    --datadir=%{_datadir} \
    --includedir=%{_includedir} \
    --libdir=%{lib32dir} \
    --libexecdir=%{_libexecdir} \
    --localstatedir=%{_localstatedir} \
    --sharedstatedir=%{_sharedstatedir} \
    --mandir=%{_mandir} \
    --infodir=%{_infodir}
make %{?_smp_mflags}
popd
%endif

%ifarch %{ix86}
%configure \
    %{?_without_mpg123} \
    %{?_without_opencl} \
    %{?_without_openal}
make %{?_smp_mflags}
%endif


%install
rm -rf %{buildroot}

%ifarch x86_64
pushd wine64-build
%make_install
popd
pushd wine32-build
%make_install
popd
%endif

%ifarch %{ix86}
%make_install
%endif


%files
%license COPYING.LIB LICENSE LICENSE.OLD
%doc ANNOUNCE AUTHORS MAINTAINERS README
# Binaries {{{
%{_bindir}/msiexec
%{_bindir}/notepad
%{_bindir}/regedit
%{_bindir}/regsvr32
%{_bindir}/wine
%{_bindir}/wine-preloader
%{_bindir}/wine64
%{_bindir}/wine64-preloader
%{_bindir}/wineboot
%{_bindir}/winecfg
%{_bindir}/wineconsole
%{_bindir}/winedbg
%{_bindir}/winedump
%{_bindir}/winefile
%{_bindir}/winemine
%{_bindir}/winepath
%{_bindir}/wineserver
%if %{with staging}
%{_bindir}/msidb
%endif
# }}}
%{_libdir}/libwine.so.*
%dir %{_libdir}/wine/
# DLL listing {{{
%{_libdir}/wine/acledit.dll.so
%{_libdir}/wine/aclui.dll.so
%{_libdir}/wine/activeds.dll.so
%{_libdir}/wine/actxprxy.dll.so
%{_libdir}/wine/adsldpc.dll.so
%{_libdir}/wine/advapi32.dll.so
%{_libdir}/wine/advpack.dll.so
%{_libdir}/wine/amstream.dll.so
%{_libdir}/wine/api-ms-win-appmodel-identity-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-appmodel-runtime-l1-1-1.dll.so
%{_libdir}/wine/api-ms-win-core-apiquery-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-appcompat-l1-1-1.dll.so
%{_libdir}/wine/api-ms-win-core-appinit-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-atoms-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-bem-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-com-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-com-l1-1-1.dll.so
%{_libdir}/wine/api-ms-win-core-com-private-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-console-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-console-l2-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-crt-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-crt-l2-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-datetime-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-datetime-l1-1-1.dll.so
%{_libdir}/wine/api-ms-win-core-debug-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-debug-l1-1-1.dll.so
%{_libdir}/wine/api-ms-win-core-delayload-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-delayload-l1-1-1.dll.so
%{_libdir}/wine/api-ms-win-core-errorhandling-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-errorhandling-l1-1-1.dll.so
%{_libdir}/wine/api-ms-win-core-errorhandling-l1-1-2.dll.so
%{_libdir}/wine/api-ms-win-core-fibers-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-fibers-l1-1-1.dll.so
%{_libdir}/wine/api-ms-win-core-file-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-file-l1-2-0.dll.so
%{_libdir}/wine/api-ms-win-core-file-l1-2-1.dll.so
%{_libdir}/wine/api-ms-win-core-file-l2-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-file-l2-1-1.dll.so
%{_libdir}/wine/api-ms-win-core-handle-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-heap-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-heap-l1-2-0.dll.so
%{_libdir}/wine/api-ms-win-core-heap-obsolete-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-interlocked-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-interlocked-l1-2-0.dll.so
%{_libdir}/wine/api-ms-win-core-io-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-io-l1-1-1.dll.so
%{_libdir}/wine/api-ms-win-core-job-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-job-l2-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-kernel32-legacy-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-kernel32-legacy-l1-1-1.dll.so
%{_libdir}/wine/api-ms-win-core-kernel32-private-l1-1-1.dll.so
%{_libdir}/wine/api-ms-win-core-libraryloader-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-libraryloader-l1-1-1.dll.so
%{_libdir}/wine/api-ms-win-core-libraryloader-l1-2-0.dll.so
%{_libdir}/wine/api-ms-win-core-libraryloader-l1-2-2.dll.so
%{_libdir}/wine/api-ms-win-core-localization-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-localization-l1-2-0.dll.so
%{_libdir}/wine/api-ms-win-core-localization-l1-2-1.dll.so
%{_libdir}/wine/api-ms-win-core-localization-l2-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-localization-obsolete-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-localization-obsolete-l1-2-0.dll.so
%{_libdir}/wine/api-ms-win-core-localization-private-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-localregistry-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-memory-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-memory-l1-1-1.dll.so
%{_libdir}/wine/api-ms-win-core-memory-l1-1-2.dll.so
%{_libdir}/wine/api-ms-win-core-misc-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-namedpipe-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-namedpipe-l1-2-0.dll.so
%{_libdir}/wine/api-ms-win-core-namespace-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-normalization-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-path-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-privateprofile-l1-1-1.dll.so
%{_libdir}/wine/api-ms-win-core-processenvironment-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-processenvironment-l1-2-0.dll.so
%{_libdir}/wine/api-ms-win-core-processthreads-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-processthreads-l1-1-1.dll.so
%{_libdir}/wine/api-ms-win-core-processthreads-l1-1-2.dll.so
%{_libdir}/wine/api-ms-win-core-profile-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-psapi-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-psapi-obsolete-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-quirks-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-realtime-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-registry-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-registry-l2-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-registryuserspecific-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-rtlsupport-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-rtlsupport-l1-2-0.dll.so
%{_libdir}/wine/api-ms-win-core-shlwapi-legacy-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-shlwapi-obsolete-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-sidebyside-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-string-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-string-l2-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-string-obsolete-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-stringansi-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-synch-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-synch-l1-2-0.dll.so
%{_libdir}/wine/api-ms-win-core-sysinfo-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-sysinfo-l1-2-0.dll.so
%{_libdir}/wine/api-ms-win-core-sysinfo-l1-2-1.dll.so
%{_libdir}/wine/api-ms-win-core-threadpool-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-threadpool-l1-2-0.dll.so
%{_libdir}/wine/api-ms-win-core-threadpool-legacy-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-threadpool-private-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-timezone-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-toolhelp-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-url-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-util-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-version-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-version-private-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-versionansi-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-windowserrorreporting-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-winrt-error-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-winrt-error-l1-1-1.dll.so
%{_libdir}/wine/api-ms-win-core-winrt-errorprivate-l1-1-1.dll.so
%{_libdir}/wine/api-ms-win-core-winrt-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-winrt-registration-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-winrt-roparameterizediid-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-winrt-string-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-wow64-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-xstate-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-xstate-l2-1-0.dll.so
%{_libdir}/wine/api-ms-win-crt-conio-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-crt-convert-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-crt-environment-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-crt-filesystem-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-crt-heap-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-crt-locale-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-crt-math-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-crt-multibyte-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-crt-private-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-crt-process-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-crt-runtime-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-crt-stdio-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-crt-string-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-crt-time-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-crt-utility-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-devices-config-l1-1-1.dll.so
%{_libdir}/wine/api-ms-win-devices-query-l1-1-1.dll.so
%{_libdir}/wine/api-ms-win-downlevel-advapi32-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-downlevel-advapi32-l2-1-0.dll.so
%{_libdir}/wine/api-ms-win-downlevel-normaliz-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-downlevel-ole32-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-downlevel-shell32-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-downlevel-shlwapi-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-downlevel-shlwapi-l2-1-0.dll.so
%{_libdir}/wine/api-ms-win-downlevel-user32-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-downlevel-version-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-dx-d3dkmt-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-eventing-classicprovider-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-eventing-consumer-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-eventing-controller-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-eventing-provider-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-eventlog-legacy-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-mm-misc-l1-1-1.dll.so
%{_libdir}/wine/api-ms-win-mm-mme-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-ntuser-dc-access-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-power-base-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-power-setting-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-rtcore-ntuser-private-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-security-activedirectoryclient-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-security-audit-l1-1-1.dll.so
%{_libdir}/wine/api-ms-win-security-base-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-security-base-l1-2-0.dll.so
%{_libdir}/wine/api-ms-win-security-base-private-l1-1-1.dll.so
%{_libdir}/wine/api-ms-win-security-credentials-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-security-grouppolicy-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-security-lsalookup-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-security-lsalookup-l1-1-1.dll.so
%{_libdir}/wine/api-ms-win-security-lsalookup-l2-1-1.dll.so
%{_libdir}/wine/api-ms-win-security-lsapolicy-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-security-sddl-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-security-systemfunctions-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-service-core-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-service-core-l1-1-1.dll.so
%{_libdir}/wine/api-ms-win-service-management-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-service-management-l2-1-0.dll.so
%{_libdir}/wine/api-ms-win-service-private-l1-1-1.dll.so
%{_libdir}/wine/api-ms-win-service-winsvc-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-service-winsvc-l1-2-0.dll.so
%{_libdir}/wine/api-ms-win-shell-shellcom-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-shell-shellfolders-l1-1-0.dll.so
%{_libdir}/wine/apphelp.dll.so
%{_libdir}/wine/appwiz.cpl.so
%{_libdir}/wine/arp.exe.so
%{_libdir}/wine/aspnet_regiis.exe.so
%{_libdir}/wine/atl.dll.so
%{_libdir}/wine/atl100.dll.so
%{_libdir}/wine/atl110.dll.so
%{_libdir}/wine/atl80.dll.so
%{_libdir}/wine/atl90.dll.so
%{_libdir}/wine/attrib.exe.so
%{_libdir}/wine/authz.dll.so
%{_libdir}/wine/avicap32.dll.so
%{_libdir}/wine/avifil32.dll.so
%{_libdir}/wine/avrt.dll.so
%{_libdir}/wine/bcrypt.dll.so
%{_libdir}/wine/bluetoothapis.dll.so
%{_libdir}/wine/browseui.dll.so
%{_libdir}/wine/bthprops.cpl.so
%{_libdir}/wine/cabarc.exe.so
%{_libdir}/wine/cabinet.dll.so
%{_libdir}/wine/cacls.exe.so
%{_libdir}/wine/capi2032.dll.so
%{_libdir}/wine/cards.dll.so
%{_libdir}/wine/cfgmgr32.dll.so
%{_libdir}/wine/clock.exe.so
%{_libdir}/wine/clusapi.dll.so
%{_libdir}/wine/cmd.exe.so
%{_libdir}/wine/combase.dll.so
%{_libdir}/wine/comcat.dll.so
%{_libdir}/wine/comctl32.dll.so
%{_libdir}/wine/comdlg32.dll.so
%{_libdir}/wine/compstui.dll.so
%{_libdir}/wine/comsvcs.dll.so
%{_libdir}/wine/concrt140.dll.so
%{_libdir}/wine/conhost.exe.so
%{_libdir}/wine/connect.dll.so
%{_libdir}/wine/control.exe.so
%{_libdir}/wine/credui.dll.so
%{_libdir}/wine/crtdll.dll.so
%{_libdir}/wine/crypt32.dll.so
%{_libdir}/wine/cryptdlg.dll.so
%{_libdir}/wine/cryptdll.dll.so
%{_libdir}/wine/cryptext.dll.so
%{_libdir}/wine/cryptnet.dll.so
%{_libdir}/wine/cryptui.dll.so
%{_libdir}/wine/cscript.exe.so
%{_libdir}/wine/ctapi32.dll.so
%{_libdir}/wine/ctl3d32.dll.so
%{_libdir}/wine/d2d1.dll.so
%{_libdir}/wine/d3d10.dll.so
%{_libdir}/wine/d3d10_1.dll.so
%{_libdir}/wine/d3d10core.dll.so
%{_libdir}/wine/d3d11.dll.so
%{_libdir}/wine/d3d8.dll.so
%{_libdir}/wine/d3d9.dll.so
%{_libdir}/wine/d3dcompiler_33.dll.so
%{_libdir}/wine/d3dcompiler_34.dll.so
%{_libdir}/wine/d3dcompiler_35.dll.so
%{_libdir}/wine/d3dcompiler_36.dll.so
%{_libdir}/wine/d3dcompiler_37.dll.so
%{_libdir}/wine/d3dcompiler_38.dll.so
%{_libdir}/wine/d3dcompiler_39.dll.so
%{_libdir}/wine/d3dcompiler_40.dll.so
%{_libdir}/wine/d3dcompiler_41.dll.so
%{_libdir}/wine/d3dcompiler_42.dll.so
%{_libdir}/wine/d3dcompiler_43.dll.so
%{_libdir}/wine/d3dcompiler_46.dll.so
%{_libdir}/wine/d3dcompiler_47.dll.so
%{_libdir}/wine/d3dim.dll.so
%{_libdir}/wine/d3drm.dll.so
%{_libdir}/wine/d3dx10_33.dll.so
%{_libdir}/wine/d3dx10_34.dll.so
%{_libdir}/wine/d3dx10_35.dll.so
%{_libdir}/wine/d3dx10_36.dll.so
%{_libdir}/wine/d3dx10_37.dll.so
%{_libdir}/wine/d3dx10_38.dll.so
%{_libdir}/wine/d3dx10_39.dll.so
%{_libdir}/wine/d3dx10_40.dll.so
%{_libdir}/wine/d3dx10_41.dll.so
%{_libdir}/wine/d3dx10_42.dll.so
%{_libdir}/wine/d3dx10_43.dll.so
%{_libdir}/wine/d3dx11_42.dll.so
%{_libdir}/wine/d3dx11_43.dll.so
%{_libdir}/wine/d3dx9_24.dll.so
%{_libdir}/wine/d3dx9_25.dll.so
%{_libdir}/wine/d3dx9_26.dll.so
%{_libdir}/wine/d3dx9_27.dll.so
%{_libdir}/wine/d3dx9_28.dll.so
%{_libdir}/wine/d3dx9_29.dll.so
%{_libdir}/wine/d3dx9_30.dll.so
%{_libdir}/wine/d3dx9_31.dll.so
%{_libdir}/wine/d3dx9_32.dll.so
%{_libdir}/wine/d3dx9_33.dll.so
%{_libdir}/wine/d3dx9_34.dll.so
%{_libdir}/wine/d3dx9_35.dll.so
%{_libdir}/wine/d3dx9_36.dll.so
%{_libdir}/wine/d3dx9_37.dll.so
%{_libdir}/wine/d3dx9_38.dll.so
%{_libdir}/wine/d3dx9_39.dll.so
%{_libdir}/wine/d3dx9_40.dll.so
%{_libdir}/wine/d3dx9_41.dll.so
%{_libdir}/wine/d3dx9_42.dll.so
%{_libdir}/wine/d3dx9_43.dll.so
%{_libdir}/wine/d3dxof.dll.so
%{_libdir}/wine/davclnt.dll.so
%{_libdir}/wine/dbgeng.dll.so
%{_libdir}/wine/dbghelp.dll.so
%{_libdir}/wine/dciman32.dll.so
%{_libdir}/wine/ddraw.dll.so
%{_libdir}/wine/ddrawex.dll.so
%{_libdir}/wine/devenum.dll.so
%{_libdir}/wine/dhcpcsvc.dll.so
%{_libdir}/wine/difxapi.dll.so
%{_libdir}/wine/dinput.dll.so
%{_libdir}/wine/dinput8.dll.so
%{_libdir}/wine/dispex.dll.so
%{_libdir}/wine/dmband.dll.so
%{_libdir}/wine/dmcompos.dll.so
%{_libdir}/wine/dmime.dll.so
%{_libdir}/wine/dmloader.dll.so
%{_libdir}/wine/dmscript.dll.so
%{_libdir}/wine/dmstyle.dll.so
%{_libdir}/wine/dmsynth.dll.so
%{_libdir}/wine/dmusic.dll.so
%{_libdir}/wine/dmusic32.dll.so
%{_libdir}/wine/dnsapi.dll.so
%{_libdir}/wine/dplay.dll.so
%{_libdir}/wine/dplayx.dll.so
%{_libdir}/wine/dpnaddr.dll.so
%{_libdir}/wine/dpnet.dll.so
%{_libdir}/wine/dpnhpast.dll.so
%{_libdir}/wine/dpnlobby.dll.so
%{_libdir}/wine/dpnsvr.exe.so
%{_libdir}/wine/dpvoice.dll.so
%{_libdir}/wine/dpwsockx.dll.so
%{_libdir}/wine/drmclien.dll.so
%{_libdir}/wine/dsound.dll.so
%{_libdir}/wine/dssenh.dll.so
%{_libdir}/wine/dswave.dll.so
%{_libdir}/wine/dwmapi.dll.so
%{_libdir}/wine/dwrite.dll.so
%{_libdir}/wine/dxdiag.exe.so
%{_libdir}/wine/dxdiagn.dll.so
%{_libdir}/wine/dxgi.dll.so
%{_libdir}/wine/dxva2.dll.so
%{_libdir}/wine/eject.exe.so
%{_libdir}/wine/esent.dll.so
%{_libdir}/wine/evr.dll.so
%{_libdir}/wine/expand.exe.so
%{_libdir}/wine/explorer.exe.so
%{_libdir}/wine/explorerframe.dll.so
%{_libdir}/wine/ext-ms-win-authz-context-l1-1-0.dll.so
%{_libdir}/wine/ext-ms-win-domainjoin-netjoin-l1-1-0.dll.so
%{_libdir}/wine/ext-ms-win-gdi-dc-create-l1-1-1.dll.so
%{_libdir}/wine/ext-ms-win-gdi-dc-l1-2-0.dll.so
%{_libdir}/wine/ext-ms-win-gdi-devcaps-l1-1-0.dll.so
%{_libdir}/wine/ext-ms-win-gdi-draw-l1-1-1.dll.so
%{_libdir}/wine/ext-ms-win-gdi-render-l1-1-0.dll.so
%{_libdir}/wine/ext-ms-win-kernel32-package-current-l1-1-0.dll.so
%{_libdir}/wine/ext-ms-win-ntuser-message-l1-1-1.dll.so
%{_libdir}/wine/ext-ms-win-ntuser-private-l1-1-1.dll.so
%{_libdir}/wine/ext-ms-win-ntuser-rectangle-ext-l1-1-0.dll.so
%{_libdir}/wine/ext-ms-win-ntuser-uicontext-ext-l1-1-0.dll.so
%{_libdir}/wine/ext-ms-win-ntuser-window-l1-1-1.dll.so
%{_libdir}/wine/ext-ms-win-rtcore-gdi-object-l1-1-0.dll.so
%{_libdir}/wine/ext-ms-win-rtcore-gdi-rgn-l1-1-0.dll.so
%{_libdir}/wine/ext-ms-win-rtcore-ntuser-dc-access-l1-1-0.dll.so
%{_libdir}/wine/ext-ms-win-rtcore-ntuser-dpi-l1-1-0.dll.so
%{_libdir}/wine/ext-ms-win-rtcore-ntuser-sysparams-l1-1-0.dll.so
%{_libdir}/wine/extrac32.exe.so
%{_libdir}/wine/faultrep.dll.so
%{_libdir}/wine/findstr.exe.so
%{_libdir}/wine/fltlib.dll.so
%{_libdir}/wine/fltmgr.sys.so
%{_libdir}/wine/fntcache.dll.so
%{_libdir}/wine/fontsub.dll.so
%{_libdir}/wine/fsutil.exe.so
%{_libdir}/wine/fusion.dll.so
%{_libdir}/wine/fwpuclnt.dll.so
%{_libdir}/wine/gameux.dll.so
%{_libdir}/wine/gdi32.dll.so
%{_libdir}/wine/gdiplus.dll.so
%{_libdir}/wine/glu32.dll.so
%{_libdir}/wine/gphoto2.ds.so
%{_libdir}/wine/gpkcsp.dll.so
%{_libdir}/wine/hal.dll.so
%{_libdir}/wine/hh.exe.so
%{_libdir}/wine/hhctrl.ocx.so
%{_libdir}/wine/hid.dll.so
%{_libdir}/wine/hidclass.sys.so
%{_libdir}/wine/hlink.dll.so
%{_libdir}/wine/hnetcfg.dll.so
%{_libdir}/wine/hostname.exe.so
%{_libdir}/wine/httpapi.dll.so
%{_libdir}/wine/icacls.exe.so
%{_libdir}/wine/iccvid.dll.so
%{_libdir}/wine/icinfo.exe.so
%{_libdir}/wine/icmp.dll.so
%{_libdir}/wine/ieframe.dll.so
%{_libdir}/wine/iexplore.exe.so
%{_libdir}/wine/imaadp32.acm.so
%{_libdir}/wine/imagehlp.dll.so
%{_libdir}/wine/imm32.dll.so
%{_libdir}/wine/inetcomm.dll.so
%{_libdir}/wine/inetcpl.cpl.so
%{_libdir}/wine/inetmib1.dll.so
%{_libdir}/wine/infosoft.dll.so
%{_libdir}/wine/initpki.dll.so
%{_libdir}/wine/inkobj.dll.so
%{_libdir}/wine/inseng.dll.so
%{_libdir}/wine/ipconfig.exe.so
%{_libdir}/wine/iphlpapi.dll.so
%{_libdir}/wine/iprop.dll.so
%{_libdir}/wine/irprops.cpl.so
%{_libdir}/wine/itircl.dll.so
%{_libdir}/wine/itss.dll.so
%{_libdir}/wine/joy.cpl.so
%{_libdir}/wine/jscript.dll.so
%{_libdir}/wine/jsproxy.dll.so
%{_libdir}/wine/kernel32.dll.so
%{_libdir}/wine/kernelbase.dll.so
%{_libdir}/wine/ksuser.dll.so
%{_libdir}/wine/ktmw32.dll.so
%{_libdir}/wine/loadperf.dll.so
%{_libdir}/wine/localspl.dll.so
%{_libdir}/wine/localui.dll.so
%{_libdir}/wine/lodctr.exe.so
%{_libdir}/wine/lz32.dll.so
%{_libdir}/wine/mapi32.dll.so
%{_libdir}/wine/mapistub.dll.so
%{_libdir}/wine/mciavi32.dll.so
%{_libdir}/wine/mcicda.dll.so
%{_libdir}/wine/mciqtz32.dll.so
%{_libdir}/wine/mciseq.dll.so
%{_libdir}/wine/mciwave.dll.so
%{_libdir}/wine/mf.dll.so
%{_libdir}/wine/mf3216.dll.so
%{_libdir}/wine/mfplat.dll.so
%{_libdir}/wine/mfreadwrite.dll.so
%{_libdir}/wine/mgmtapi.dll.so
%{_libdir}/wine/midimap.dll.so
%{_libdir}/wine/mlang.dll.so
%{_libdir}/wine/mmcndmgr.dll.so
%{_libdir}/wine/mmdevapi.dll.so
%{_libdir}/wine/mofcomp.exe.so
%{_libdir}/wine/mountmgr.sys.so
%{_libdir}/wine/mpr.dll.so
%{_libdir}/wine/mprapi.dll.so
%{_libdir}/wine/msacm32.dll.so
%{_libdir}/wine/msacm32.drv.so
%{_libdir}/wine/msadp32.acm.so
%{_libdir}/wine/msasn1.dll.so
%{_libdir}/wine/mscat32.dll.so
%{_libdir}/wine/mscms.dll.so
%{_libdir}/wine/mscoree.dll.so
%{_libdir}/wine/msctf.dll.so
%{_libdir}/wine/msctfp.dll.so
%{_libdir}/wine/msdaps.dll.so
%{_libdir}/wine/msdelta.dll.so
%{_libdir}/wine/msdmo.dll.so
%{_libdir}/wine/msdrm.dll.so
%{_libdir}/wine/msftedit.dll.so
%{_libdir}/wine/msg711.acm.so
%{_libdir}/wine/msgsm32.acm.so
%{_libdir}/wine/mshta.exe.so
%{_libdir}/wine/mshtml.dll.so
%{_libdir}/wine/mshtml.tlb.so
%{_libdir}/wine/msi.dll.so
%{_libdir}/wine/msident.dll.so
%{_libdir}/wine/msiexec.exe.so
%{_libdir}/wine/msimg32.dll.so
%{_libdir}/wine/msimsg.dll.so
%{_libdir}/wine/msimtf.dll.so
%{_libdir}/wine/msinfo32.exe.so
%{_libdir}/wine/msisip.dll.so
%{_libdir}/wine/msisys.ocx.so
%{_libdir}/wine/msls31.dll.so
%{_libdir}/wine/msnet32.dll.so
%{_libdir}/wine/mspatcha.dll.so
%{_libdir}/wine/msports.dll.so
%{_libdir}/wine/msrle32.dll.so
%{_libdir}/wine/msscript.ocx.so
%{_libdir}/wine/mssign32.dll.so
%{_libdir}/wine/mssip32.dll.so
%{_libdir}/wine/mstask.dll.so
%{_libdir}/wine/msvcirt.dll.so
%{_libdir}/wine/msvcm80.dll.so
%{_libdir}/wine/msvcm90.dll.so
%{_libdir}/wine/msvcp100.dll.so
%{_libdir}/wine/msvcp110.dll.so
%{_libdir}/wine/msvcp120.dll.so
%{_libdir}/wine/msvcp120_app.dll.so
%{_libdir}/wine/msvcp140.dll.so
%{_libdir}/wine/msvcp60.dll.so
%{_libdir}/wine/msvcp70.dll.so
%{_libdir}/wine/msvcp71.dll.so
%{_libdir}/wine/msvcp80.dll.so
%{_libdir}/wine/msvcp90.dll.so
%{_libdir}/wine/msvcr100.dll.so
%{_libdir}/wine/msvcr110.dll.so
%{_libdir}/wine/msvcr120.dll.so
%{_libdir}/wine/msvcr120_app.dll.so
%{_libdir}/wine/msvcr70.dll.so
%{_libdir}/wine/msvcr71.dll.so
%{_libdir}/wine/msvcr80.dll.so
%{_libdir}/wine/msvcr90.dll.so
%{_libdir}/wine/msvcrt.dll.so
%{_libdir}/wine/msvcrt20.dll.so
%{_libdir}/wine/msvcrt40.dll.so
%{_libdir}/wine/msvcrtd.dll.so
%{_libdir}/wine/msvfw32.dll.so
%{_libdir}/wine/msvidc32.dll.so
%{_libdir}/wine/mswsock.dll.so
%{_libdir}/wine/msxml.dll.so
%{_libdir}/wine/msxml2.dll.so
%{_libdir}/wine/msxml3.dll.so
%{_libdir}/wine/msxml4.dll.so
%{_libdir}/wine/msxml6.dll.so
%{_libdir}/wine/mtxdm.dll.so
%{_libdir}/wine/ncrypt.dll.so
%{_libdir}/wine/nddeapi.dll.so
%{_libdir}/wine/ndis.sys.so
%{_libdir}/wine/net.exe.so
%{_libdir}/wine/netapi32.dll.so
%{_libdir}/wine/netcfgx.dll.so
%{_libdir}/wine/netprofm.dll.so
%{_libdir}/wine/netsh.exe.so
%{_libdir}/wine/netstat.exe.so
%{_libdir}/wine/newdev.dll.so
%{_libdir}/wine/ngen.exe.so
%{_libdir}/wine/normaliz.dll.so
%{_libdir}/wine/notepad.exe.so
%{_libdir}/wine/npmshtml.dll.so
%{_libdir}/wine/npptools.dll.so
%{_libdir}/wine/ntdll.dll.so
%{_libdir}/wine/ntdsapi.dll.so
%{_libdir}/wine/ntoskrnl.exe.so
%{_libdir}/wine/ntprint.dll.so
%{_libdir}/wine/objsel.dll.so
%{_libdir}/wine/odbc32.dll.so
%{_libdir}/wine/odbccp32.dll.so
%{_libdir}/wine/odbccu32.dll.so
%{_libdir}/wine/ole32.dll.so
%{_libdir}/wine/oleacc.dll.so
%{_libdir}/wine/oleaut32.dll.so
%{_libdir}/wine/olecli32.dll.so
%{_libdir}/wine/oledb32.dll.so
%{_libdir}/wine/oledlg.dll.so
%{_libdir}/wine/olepro32.dll.so
%{_libdir}/wine/olesvr32.dll.so
%{_libdir}/wine/olethk32.dll.so
%{_libdir}/wine/oleview.exe.so
%{_libdir}/wine/opengl32.dll.so
%{_libdir}/wine/packager.dll.so
%{_libdir}/wine/pdh.dll.so
%{_libdir}/wine/photometadatahandler.dll.so
%{_libdir}/wine/pidgen.dll.so
%{_libdir}/wine/ping.exe.so
%{_libdir}/wine/plugplay.exe.so
%{_libdir}/wine/powrprof.dll.so
%{_libdir}/wine/presentationfontcache.exe.so
%{_libdir}/wine/printui.dll.so
%{_libdir}/wine/prntvpt.dll.so
%{_libdir}/wine/progman.exe.so
%{_libdir}/wine/propsys.dll.so
%{_libdir}/wine/psapi.dll.so
%{_libdir}/wine/pstorec.dll.so
%{_libdir}/wine/qcap.dll.so
%{_libdir}/wine/qedit.dll.so
%{_libdir}/wine/qmgr.dll.so
%{_libdir}/wine/qmgrprxy.dll.so
%{_libdir}/wine/quartz.dll.so
%{_libdir}/wine/query.dll.so
%{_libdir}/wine/rasapi32.dll.so
%{_libdir}/wine/rasdlg.dll.so
%{_libdir}/wine/reg.exe.so
%{_libdir}/wine/regapi.dll.so
%{_libdir}/wine/regasm.exe.so
%{_libdir}/wine/regedit.exe.so
%{_libdir}/wine/regsvcs.exe.so
%{_libdir}/wine/regsvr32.exe.so
%{_libdir}/wine/resutils.dll.so
%{_libdir}/wine/riched20.dll.so
%{_libdir}/wine/riched32.dll.so
%{_libdir}/wine/rpcrt4.dll.so
%{_libdir}/wine/rpcss.exe.so
%{_libdir}/wine/rsabase.dll.so
%{_libdir}/wine/rsaenh.dll.so
%{_libdir}/wine/rstrtmgr.dll.so
%{_libdir}/wine/rtutils.dll.so
%{_libdir}/wine/rundll32.exe.so
%{_libdir}/wine/samlib.dll.so
%{_libdir}/wine/sane.ds.so
%{_libdir}/wine/sc.exe.so
%{_libdir}/wine/scarddlg.dll.so
%{_libdir}/wine/sccbase.dll.so
%{_libdir}/wine/schannel.dll.so
%{_libdir}/wine/schedsvc.dll.so
%{_libdir}/wine/schtasks.exe.so
%{_libdir}/wine/scrobj.dll.so
%{_libdir}/wine/scrrun.dll.so
%{_libdir}/wine/scsiport.sys.so
%{_libdir}/wine/sdbinst.exe.so
%{_libdir}/wine/secedit.exe.so
%{_libdir}/wine/secur32.dll.so
%{_libdir}/wine/security.dll.so
%{_libdir}/wine/sensapi.dll.so
%{_libdir}/wine/serialui.dll.so
%{_libdir}/wine/servicemodelreg.exe.so
%{_libdir}/wine/services.exe.so
%{_libdir}/wine/setupapi.dll.so
%{_libdir}/wine/sfc.dll.so
%{_libdir}/wine/sfc_os.dll.so
%{_libdir}/wine/shdoclc.dll.so
%{_libdir}/wine/shdocvw.dll.so
%{_libdir}/wine/shell32.dll.so
%{_libdir}/wine/shfolder.dll.so
%{_libdir}/wine/shlwapi.dll.so
%{_libdir}/wine/shutdown.exe.so
%{_libdir}/wine/slbcsp.dll.so
%{_libdir}/wine/slc.dll.so
%{_libdir}/wine/snmpapi.dll.so
%{_libdir}/wine/softpub.dll.so
%{_libdir}/wine/spoolss.dll.so
%{_libdir}/wine/spoolsv.exe.so
%{_libdir}/wine/sspicli.dll.so
%{_libdir}/wine/start.exe.so
%{_libdir}/wine/stdole2.tlb.so
%{_libdir}/wine/stdole32.tlb.so
%{_libdir}/wine/sti.dll.so
%{_libdir}/wine/subst.exe.so
%{_libdir}/wine/svchost.exe.so
%{_libdir}/wine/svrapi.dll.so
%{_libdir}/wine/sxs.dll.so
%{_libdir}/wine/systeminfo.exe.so
%{_libdir}/wine/t2embed.dll.so
%{_libdir}/wine/tapi32.dll.so
%{_libdir}/wine/taskkill.exe.so
%{_libdir}/wine/tasklist.exe.so
%{_libdir}/wine/taskmgr.exe.so
%{_libdir}/wine/taskschd.dll.so
%{_libdir}/wine/tdh.dll.so
%{_libdir}/wine/tdi.sys.so
%{_libdir}/wine/termsv.exe.so
%{_libdir}/wine/traffic.dll.so
%{_libdir}/wine/twain_32.dll.so
%{_libdir}/wine/ucrtbase.dll.so
%{_libdir}/wine/uiautomationcore.dll.so
%{_libdir}/wine/unicows.dll.so
%{_libdir}/wine/uninstaller.exe.so
%{_libdir}/wine/unlodctr.exe.so
%{_libdir}/wine/updspapi.dll.so
%{_libdir}/wine/url.dll.so
%{_libdir}/wine/urlmon.dll.so
%{_libdir}/wine/usbd.sys.so
%{_libdir}/wine/user32.dll.so
%{_libdir}/wine/userenv.dll.so
%{_libdir}/wine/usp10.dll.so
%{_libdir}/wine/uxtheme.dll.so
%{_libdir}/wine/vbscript.dll.so
%{_libdir}/wine/vcomp.dll.so
%{_libdir}/wine/vcomp100.dll.so
%{_libdir}/wine/vcomp110.dll.so
%{_libdir}/wine/vcomp120.dll.so
%{_libdir}/wine/vcomp140.dll.so
%{_libdir}/wine/vcomp90.dll.so
%{_libdir}/wine/vcruntime140.dll.so
%{_libdir}/wine/vdmdbg.dll.so
%{_libdir}/wine/version.dll.so
%{_libdir}/wine/view.exe.so
%{_libdir}/wine/virtdisk.dll.so
%{_libdir}/wine/vssapi.dll.so
%{_libdir}/wine/wbemdisp.dll.so
%{_libdir}/wine/wbemprox.dll.so
%{_libdir}/wine/webservices.dll.so
%{_libdir}/wine/wer.dll.so
%{_libdir}/wine/wevtapi.dll.so
%{_libdir}/wine/wevtutil.exe.so
%{_libdir}/wine/wiaservc.dll.so
%{_libdir}/wine/wimgapi.dll.so
%{_libdir}/wine/windowscodecs.dll.so
%{_libdir}/wine/windowscodecsext.dll.so
%{_libdir}/wine/winealsa.drv.so
%{_libdir}/wine/wineboot.exe.so
%{_libdir}/wine/winebrowser.exe.so
%{_libdir}/wine/winebus.sys.so
%{_libdir}/wine/winecfg.exe.so
%{_libdir}/wine/wineconsole.exe.so
%{_libdir}/wine/wined3d.dll.so
%{_libdir}/wine/winedbg.exe.so
%{_libdir}/wine/winedevice.exe.so
%{_libdir}/wine/winefile.exe.so
%{_libdir}/wine/winegstreamer.dll.so
%{_libdir}/wine/winehid.sys.so
%{_libdir}/wine/winejoystick.drv.so
%{_libdir}/wine/winemapi.dll.so
%{_libdir}/wine/winemenubuilder.exe.so
%{_libdir}/wine/winemine.exe.so
%{_libdir}/wine/winemsibuilder.exe.so
%{_libdir}/wine/winepath.exe.so
%{_libdir}/wine/wineps.drv.so
%{_libdir}/wine/winepulse.drv.so
%{_libdir}/wine/winex11.drv.so
%{_libdir}/wine/wing32.dll.so
%{_libdir}/wine/winhlp32.exe.so
%{_libdir}/wine/winhttp.dll.so
%{_libdir}/wine/wininet.dll.so
%{_libdir}/wine/winmm.dll.so
%{_libdir}/wine/winnls32.dll.so
%{_libdir}/wine/winscard.dll.so
%{_libdir}/wine/winspool.drv.so
%{_libdir}/wine/winsta.dll.so
%{_libdir}/wine/wintab32.dll.so
%{_libdir}/wine/wintrust.dll.so
%{_libdir}/wine/winusb.dll.so
%{_libdir}/wine/winver.exe.so
%{_libdir}/wine/wlanapi.dll.so
%{_libdir}/wine/wldap32.dll.so
%{_libdir}/wine/wmasf.dll.so
%{_libdir}/wine/wmi.dll.so
%{_libdir}/wine/wmic.exe.so
%{_libdir}/wine/wmiutils.dll.so
%{_libdir}/wine/wmp.dll.so
%{_libdir}/wine/wmplayer.exe.so
%{_libdir}/wine/wmvcore.dll.so
%{_libdir}/wine/wnaspi32.dll.so
%{_libdir}/wine/wordpad.exe.so
%{_libdir}/wine/wpc.dll.so
%{_libdir}/wine/wpcap.dll.so
%{_libdir}/wine/write.exe.so
%{_libdir}/wine/ws2_32.dll.so
%{_libdir}/wine/wscript.exe.so
%{_libdir}/wine/wsdapi.dll.so
%{_libdir}/wine/wshom.ocx.so
%{_libdir}/wine/wsnmp32.dll.so
%{_libdir}/wine/wsock32.dll.so
%{_libdir}/wine/wtsapi32.dll.so
%{_libdir}/wine/wuapi.dll.so
%{_libdir}/wine/wuaueng.dll.so
%{_libdir}/wine/wusa.exe.so
%{_libdir}/wine/xcopy.exe.so
%{_libdir}/wine/xinput1_1.dll.so
%{_libdir}/wine/xinput1_2.dll.so
%{_libdir}/wine/xinput1_3.dll.so
%{_libdir}/wine/xinput1_4.dll.so
%{_libdir}/wine/xinput9_1_0.dll.so
%{_libdir}/wine/xmllite.dll.so
%{_libdir}/wine/xolehlp.dll.so
%{_libdir}/wine/xpsprint.dll.so
%{_libdir}/wine/xpssvcs.dll.so

%if %{with staging}
%{_libdir}/wine/api-ms-win-core-heap-l2-1-0.dll.so
%{_libdir}/wine/api-ms-win-core-shlwapi-obsolete-l1-2-0.dll.so
%{_libdir}/wine/api-ms-win-rtcore-ntuser-draw-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-rtcore-ntuser-window-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-shcore-obsolete-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-shcore-stream-l1-1-0.dll.so
%{_libdir}/wine/api-ms-win-shcore-thread-l1-1-0.dll.so
%{_libdir}/wine/dxgkrnl.sys.so
%{_libdir}/wine/dxgmms1.sys.so
%{_libdir}/wine/ext-ms-win-appmodel-usercontext-l1-1-0.dll.so
%{_libdir}/wine/ext-ms-win-ntuser-mouse-l1-1-0.dll.so
%{_libdir}/wine/ext-ms-win-rtcore-ntuser-syscolors-l1-1-0.dll.so
%{_libdir}/wine/ext-ms-win-uxtheme-themes-l1-1-0.dll.so
%{_libdir}/wine/ext-ms-win-xaml-pal-l1-1-0.dll.so
%{_libdir}/wine/feclient.dll.so
%{_libdir}/wine/iertutil.dll.so
%{_libdir}/wine/msidb.exe.so
%{_libdir}/wine/nvapi64.dll.so
%{_libdir}/wine/nvcuda.dll.so
%{_libdir}/wine/nvcuvid.dll.so
%{_libdir}/wine/nvencodeapi64.dll.so
%{_libdir}/wine/shcore.dll.so
%{_libdir}/wine/uxtheme-gtk.dll.so
%{_libdir}/wine/vulkan-1.dll.so
%{_libdir}/wine/vulkan.dll.so
%{_libdir}/wine/win32k.sys.so
%{_libdir}/wine/wined3d-csmt.dll.so
%{_libdir}/wine/wuauserv.exe.so
%endif

%if %{with mpg123}
%{_libdir}/wine/winemp3.acm.so
%endif

%if %{with opencl}
%{_libdir}/wine/opencl.dll.so
%endif

%if %{with openal}
%{_libdir}/wine/openal32.dll.so
%{_libdir}/wine/x3daudio1_0.dll.so
%{_libdir}/wine/x3daudio1_1.dll.so
%{_libdir}/wine/x3daudio1_2.dll.so
%{_libdir}/wine/x3daudio1_3.dll.so
%{_libdir}/wine/x3daudio1_4.dll.so
%{_libdir}/wine/x3daudio1_5.dll.so
%{_libdir}/wine/x3daudio1_6.dll.so
%{_libdir}/wine/x3daudio1_7.dll.so
%{_libdir}/wine/xapofx1_1.dll.so
%{_libdir}/wine/xapofx1_2.dll.so
%{_libdir}/wine/xapofx1_3.dll.so
%{_libdir}/wine/xapofx1_4.dll.so
%{_libdir}/wine/xapofx1_5.dll.so
%{_libdir}/wine/xaudio2_0.dll.so
%{_libdir}/wine/xaudio2_1.dll.so
%{_libdir}/wine/xaudio2_2.dll.so
%{_libdir}/wine/xaudio2_3.dll.so
%{_libdir}/wine/xaudio2_4.dll.so
%{_libdir}/wine/xaudio2_5.dll.so
%{_libdir}/wine/xaudio2_6.dll.so
%{_libdir}/wine/xaudio2_7.dll.so
%{_libdir}/wine/xaudio2_8.dll.so
%{_libdir}/wine/xaudio2_9.dll.so
%endif
# }}}
%{_libdir}/wine/fakedlls/

%ifarch x86_64
%{lib32dir}/libwine.so.*
%dir %{lib32dir}/wine/
# DLL listing {{{
%{lib32dir}/wine/acledit.dll.so
%{lib32dir}/wine/aclui.dll.so
%{lib32dir}/wine/activeds.dll.so
%{lib32dir}/wine/actxprxy.dll.so
%{lib32dir}/wine/adsldpc.dll.so
%{lib32dir}/wine/advapi32.dll.so
%{lib32dir}/wine/advpack.dll.so
%{lib32dir}/wine/amstream.dll.so
%{lib32dir}/wine/api-ms-win-appmodel-identity-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-appmodel-runtime-l1-1-1.dll.so
%{lib32dir}/wine/api-ms-win-core-apiquery-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-appcompat-l1-1-1.dll.so
%{lib32dir}/wine/api-ms-win-core-appinit-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-atoms-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-bem-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-com-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-com-l1-1-1.dll.so
%{lib32dir}/wine/api-ms-win-core-com-private-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-console-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-console-l2-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-crt-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-crt-l2-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-datetime-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-datetime-l1-1-1.dll.so
%{lib32dir}/wine/api-ms-win-core-debug-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-debug-l1-1-1.dll.so
%{lib32dir}/wine/api-ms-win-core-delayload-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-delayload-l1-1-1.dll.so
%{lib32dir}/wine/api-ms-win-core-errorhandling-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-errorhandling-l1-1-1.dll.so
%{lib32dir}/wine/api-ms-win-core-errorhandling-l1-1-2.dll.so
%{lib32dir}/wine/api-ms-win-core-fibers-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-fibers-l1-1-1.dll.so
%{lib32dir}/wine/api-ms-win-core-file-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-file-l1-2-0.dll.so
%{lib32dir}/wine/api-ms-win-core-file-l1-2-1.dll.so
%{lib32dir}/wine/api-ms-win-core-file-l2-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-file-l2-1-1.dll.so
%{lib32dir}/wine/api-ms-win-core-handle-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-heap-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-heap-l1-2-0.dll.so
%{lib32dir}/wine/api-ms-win-core-heap-obsolete-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-interlocked-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-interlocked-l1-2-0.dll.so
%{lib32dir}/wine/api-ms-win-core-io-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-io-l1-1-1.dll.so
%{lib32dir}/wine/api-ms-win-core-job-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-job-l2-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-kernel32-legacy-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-kernel32-legacy-l1-1-1.dll.so
%{lib32dir}/wine/api-ms-win-core-kernel32-private-l1-1-1.dll.so
%{lib32dir}/wine/api-ms-win-core-libraryloader-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-libraryloader-l1-1-1.dll.so
%{lib32dir}/wine/api-ms-win-core-libraryloader-l1-2-0.dll.so
%{lib32dir}/wine/api-ms-win-core-libraryloader-l1-2-2.dll.so
%{lib32dir}/wine/api-ms-win-core-localization-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-localization-l1-2-0.dll.so
%{lib32dir}/wine/api-ms-win-core-localization-l1-2-1.dll.so
%{lib32dir}/wine/api-ms-win-core-localization-l2-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-localization-obsolete-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-localization-obsolete-l1-2-0.dll.so
%{lib32dir}/wine/api-ms-win-core-localization-private-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-localregistry-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-memory-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-memory-l1-1-1.dll.so
%{lib32dir}/wine/api-ms-win-core-memory-l1-1-2.dll.so
%{lib32dir}/wine/api-ms-win-core-misc-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-namedpipe-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-namedpipe-l1-2-0.dll.so
%{lib32dir}/wine/api-ms-win-core-namespace-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-normalization-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-path-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-privateprofile-l1-1-1.dll.so
%{lib32dir}/wine/api-ms-win-core-processenvironment-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-processenvironment-l1-2-0.dll.so
%{lib32dir}/wine/api-ms-win-core-processthreads-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-processthreads-l1-1-1.dll.so
%{lib32dir}/wine/api-ms-win-core-processthreads-l1-1-2.dll.so
%{lib32dir}/wine/api-ms-win-core-profile-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-psapi-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-psapi-obsolete-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-quirks-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-realtime-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-registry-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-registry-l2-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-registryuserspecific-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-rtlsupport-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-rtlsupport-l1-2-0.dll.so
%{lib32dir}/wine/api-ms-win-core-shlwapi-legacy-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-shlwapi-obsolete-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-sidebyside-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-string-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-string-l2-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-string-obsolete-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-stringansi-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-synch-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-synch-l1-2-0.dll.so
%{lib32dir}/wine/api-ms-win-core-sysinfo-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-sysinfo-l1-2-0.dll.so
%{lib32dir}/wine/api-ms-win-core-sysinfo-l1-2-1.dll.so
%{lib32dir}/wine/api-ms-win-core-threadpool-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-threadpool-l1-2-0.dll.so
%{lib32dir}/wine/api-ms-win-core-threadpool-legacy-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-threadpool-private-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-timezone-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-toolhelp-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-url-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-util-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-version-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-version-private-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-versionansi-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-windowserrorreporting-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-winrt-error-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-winrt-error-l1-1-1.dll.so
%{lib32dir}/wine/api-ms-win-core-winrt-errorprivate-l1-1-1.dll.so
%{lib32dir}/wine/api-ms-win-core-winrt-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-winrt-registration-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-winrt-roparameterizediid-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-winrt-string-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-wow64-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-xstate-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-xstate-l2-1-0.dll.so
%{lib32dir}/wine/api-ms-win-crt-conio-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-crt-convert-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-crt-environment-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-crt-filesystem-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-crt-heap-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-crt-locale-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-crt-math-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-crt-multibyte-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-crt-private-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-crt-process-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-crt-runtime-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-crt-stdio-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-crt-string-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-crt-time-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-crt-utility-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-devices-config-l1-1-1.dll.so
%{lib32dir}/wine/api-ms-win-devices-query-l1-1-1.dll.so
%{lib32dir}/wine/api-ms-win-downlevel-advapi32-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-downlevel-advapi32-l2-1-0.dll.so
%{lib32dir}/wine/api-ms-win-downlevel-normaliz-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-downlevel-ole32-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-downlevel-shell32-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-downlevel-shlwapi-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-downlevel-shlwapi-l2-1-0.dll.so
%{lib32dir}/wine/api-ms-win-downlevel-user32-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-downlevel-version-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-dx-d3dkmt-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-eventing-classicprovider-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-eventing-consumer-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-eventing-controller-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-eventing-provider-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-eventlog-legacy-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-mm-misc-l1-1-1.dll.so
%{lib32dir}/wine/api-ms-win-mm-mme-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-ntuser-dc-access-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-power-base-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-power-setting-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-rtcore-ntuser-private-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-security-activedirectoryclient-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-security-audit-l1-1-1.dll.so
%{lib32dir}/wine/api-ms-win-security-base-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-security-base-l1-2-0.dll.so
%{lib32dir}/wine/api-ms-win-security-base-private-l1-1-1.dll.so
%{lib32dir}/wine/api-ms-win-security-credentials-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-security-grouppolicy-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-security-lsalookup-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-security-lsalookup-l1-1-1.dll.so
%{lib32dir}/wine/api-ms-win-security-lsalookup-l2-1-1.dll.so
%{lib32dir}/wine/api-ms-win-security-lsapolicy-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-security-sddl-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-security-systemfunctions-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-service-core-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-service-core-l1-1-1.dll.so
%{lib32dir}/wine/api-ms-win-service-management-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-service-management-l2-1-0.dll.so
%{lib32dir}/wine/api-ms-win-service-private-l1-1-1.dll.so
%{lib32dir}/wine/api-ms-win-service-winsvc-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-service-winsvc-l1-2-0.dll.so
%{lib32dir}/wine/api-ms-win-shell-shellcom-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-shell-shellfolders-l1-1-0.dll.so
%{lib32dir}/wine/apphelp.dll.so
%{lib32dir}/wine/appwiz.cpl.so
%{lib32dir}/wine/arp.exe.so
%{lib32dir}/wine/aspnet_regiis.exe.so
%{lib32dir}/wine/atl.dll.so
%{lib32dir}/wine/atl100.dll.so
%{lib32dir}/wine/atl110.dll.so
%{lib32dir}/wine/atl80.dll.so
%{lib32dir}/wine/atl90.dll.so
%{lib32dir}/wine/attrib.exe.so
%{lib32dir}/wine/authz.dll.so
%{lib32dir}/wine/avicap32.dll.so
%{lib32dir}/wine/avifil32.dll.so
%{lib32dir}/wine/avifile.dll16.so
%{lib32dir}/wine/avrt.dll.so
%{lib32dir}/wine/bcrypt.dll.so
%{lib32dir}/wine/bluetoothapis.dll.so
%{lib32dir}/wine/browseui.dll.so
%{lib32dir}/wine/bthprops.cpl.so
%{lib32dir}/wine/cabarc.exe.so
%{lib32dir}/wine/cabinet.dll.so
%{lib32dir}/wine/cacls.exe.so
%{lib32dir}/wine/capi2032.dll.so
%{lib32dir}/wine/cards.dll.so
%{lib32dir}/wine/cfgmgr32.dll.so
%{lib32dir}/wine/clock.exe.so
%{lib32dir}/wine/clusapi.dll.so
%{lib32dir}/wine/cmd.exe.so
%{lib32dir}/wine/combase.dll.so
%{lib32dir}/wine/comcat.dll.so
%{lib32dir}/wine/comctl32.dll.so
%{lib32dir}/wine/comdlg32.dll.so
%{lib32dir}/wine/comm.drv16.so
%{lib32dir}/wine/commdlg.dll16.so
%{lib32dir}/wine/compobj.dll16.so
%{lib32dir}/wine/compstui.dll.so
%{lib32dir}/wine/comsvcs.dll.so
%{lib32dir}/wine/concrt140.dll.so
%{lib32dir}/wine/conhost.exe.so
%{lib32dir}/wine/connect.dll.so
%{lib32dir}/wine/control.exe.so
%{lib32dir}/wine/credui.dll.so
%{lib32dir}/wine/crtdll.dll.so
%{lib32dir}/wine/crypt32.dll.so
%{lib32dir}/wine/cryptdlg.dll.so
%{lib32dir}/wine/cryptdll.dll.so
%{lib32dir}/wine/cryptext.dll.so
%{lib32dir}/wine/cryptnet.dll.so
%{lib32dir}/wine/cryptui.dll.so
%{lib32dir}/wine/cscript.exe.so
%{lib32dir}/wine/ctapi32.dll.so
%{lib32dir}/wine/ctl3d.dll16.so
%{lib32dir}/wine/ctl3d32.dll.so
%{lib32dir}/wine/ctl3dv2.dll16.so
%{lib32dir}/wine/d2d1.dll.so
%{lib32dir}/wine/d3d10.dll.so
%{lib32dir}/wine/d3d10_1.dll.so
%{lib32dir}/wine/d3d10core.dll.so
%{lib32dir}/wine/d3d11.dll.so
%{lib32dir}/wine/d3d8.dll.so
%{lib32dir}/wine/d3d9.dll.so
%{lib32dir}/wine/d3dcompiler_33.dll.so
%{lib32dir}/wine/d3dcompiler_34.dll.so
%{lib32dir}/wine/d3dcompiler_35.dll.so
%{lib32dir}/wine/d3dcompiler_36.dll.so
%{lib32dir}/wine/d3dcompiler_37.dll.so
%{lib32dir}/wine/d3dcompiler_38.dll.so
%{lib32dir}/wine/d3dcompiler_39.dll.so
%{lib32dir}/wine/d3dcompiler_40.dll.so
%{lib32dir}/wine/d3dcompiler_41.dll.so
%{lib32dir}/wine/d3dcompiler_42.dll.so
%{lib32dir}/wine/d3dcompiler_43.dll.so
%{lib32dir}/wine/d3dcompiler_46.dll.so
%{lib32dir}/wine/d3dcompiler_47.dll.so
%{lib32dir}/wine/d3dim.dll.so
%{lib32dir}/wine/d3drm.dll.so
%{lib32dir}/wine/d3dx10_33.dll.so
%{lib32dir}/wine/d3dx10_34.dll.so
%{lib32dir}/wine/d3dx10_35.dll.so
%{lib32dir}/wine/d3dx10_36.dll.so
%{lib32dir}/wine/d3dx10_37.dll.so
%{lib32dir}/wine/d3dx10_38.dll.so
%{lib32dir}/wine/d3dx10_39.dll.so
%{lib32dir}/wine/d3dx10_40.dll.so
%{lib32dir}/wine/d3dx10_41.dll.so
%{lib32dir}/wine/d3dx10_42.dll.so
%{lib32dir}/wine/d3dx10_43.dll.so
%{lib32dir}/wine/d3dx11_42.dll.so
%{lib32dir}/wine/d3dx11_43.dll.so
%{lib32dir}/wine/d3dx9_24.dll.so
%{lib32dir}/wine/d3dx9_25.dll.so
%{lib32dir}/wine/d3dx9_26.dll.so
%{lib32dir}/wine/d3dx9_27.dll.so
%{lib32dir}/wine/d3dx9_28.dll.so
%{lib32dir}/wine/d3dx9_29.dll.so
%{lib32dir}/wine/d3dx9_30.dll.so
%{lib32dir}/wine/d3dx9_31.dll.so
%{lib32dir}/wine/d3dx9_32.dll.so
%{lib32dir}/wine/d3dx9_33.dll.so
%{lib32dir}/wine/d3dx9_34.dll.so
%{lib32dir}/wine/d3dx9_35.dll.so
%{lib32dir}/wine/d3dx9_36.dll.so
%{lib32dir}/wine/d3dx9_37.dll.so
%{lib32dir}/wine/d3dx9_38.dll.so
%{lib32dir}/wine/d3dx9_39.dll.so
%{lib32dir}/wine/d3dx9_40.dll.so
%{lib32dir}/wine/d3dx9_41.dll.so
%{lib32dir}/wine/d3dx9_42.dll.so
%{lib32dir}/wine/d3dx9_43.dll.so
%{lib32dir}/wine/d3dxof.dll.so
%{lib32dir}/wine/davclnt.dll.so
%{lib32dir}/wine/dbgeng.dll.so
%{lib32dir}/wine/dbghelp.dll.so
%{lib32dir}/wine/dciman32.dll.so
%{lib32dir}/wine/ddeml.dll16.so
%{lib32dir}/wine/ddraw.dll.so
%{lib32dir}/wine/ddrawex.dll.so
%{lib32dir}/wine/devenum.dll.so
%{lib32dir}/wine/dhcpcsvc.dll.so
%{lib32dir}/wine/difxapi.dll.so
%{lib32dir}/wine/dinput.dll.so
%{lib32dir}/wine/dinput8.dll.so
%{lib32dir}/wine/dispdib.dll16.so
%{lib32dir}/wine/dispex.dll.so
%{lib32dir}/wine/display.drv16.so
%{lib32dir}/wine/dmband.dll.so
%{lib32dir}/wine/dmcompos.dll.so
%{lib32dir}/wine/dmime.dll.so
%{lib32dir}/wine/dmloader.dll.so
%{lib32dir}/wine/dmscript.dll.so
%{lib32dir}/wine/dmstyle.dll.so
%{lib32dir}/wine/dmsynth.dll.so
%{lib32dir}/wine/dmusic.dll.so
%{lib32dir}/wine/dmusic32.dll.so
%{lib32dir}/wine/dnsapi.dll.so
%{lib32dir}/wine/dplay.dll.so
%{lib32dir}/wine/dplayx.dll.so
%{lib32dir}/wine/dpnaddr.dll.so
%{lib32dir}/wine/dpnet.dll.so
%{lib32dir}/wine/dpnhpast.dll.so
%{lib32dir}/wine/dpnlobby.dll.so
%{lib32dir}/wine/dpnsvr.exe.so
%{lib32dir}/wine/dpvoice.dll.so
%{lib32dir}/wine/dpwsockx.dll.so
%{lib32dir}/wine/drmclien.dll.so
%{lib32dir}/wine/dsound.dll.so
%{lib32dir}/wine/dssenh.dll.so
%{lib32dir}/wine/dswave.dll.so
%{lib32dir}/wine/dwmapi.dll.so
%{lib32dir}/wine/dwrite.dll.so
%{lib32dir}/wine/dxdiag.exe.so
%{lib32dir}/wine/dxdiagn.dll.so
%{lib32dir}/wine/dxgi.dll.so
%{lib32dir}/wine/dxva2.dll.so
%{lib32dir}/wine/eject.exe.so
%{lib32dir}/wine/esent.dll.so
%{lib32dir}/wine/evr.dll.so
%{lib32dir}/wine/expand.exe.so
%{lib32dir}/wine/explorer.exe.so
%{lib32dir}/wine/explorerframe.dll.so
%{lib32dir}/wine/ext-ms-win-authz-context-l1-1-0.dll.so
%{lib32dir}/wine/ext-ms-win-domainjoin-netjoin-l1-1-0.dll.so
%{lib32dir}/wine/ext-ms-win-gdi-dc-create-l1-1-1.dll.so
%{lib32dir}/wine/ext-ms-win-gdi-dc-l1-2-0.dll.so
%{lib32dir}/wine/ext-ms-win-gdi-devcaps-l1-1-0.dll.so
%{lib32dir}/wine/ext-ms-win-gdi-draw-l1-1-1.dll.so
%{lib32dir}/wine/ext-ms-win-gdi-render-l1-1-0.dll.so
%{lib32dir}/wine/ext-ms-win-kernel32-package-current-l1-1-0.dll.so
%{lib32dir}/wine/ext-ms-win-ntuser-message-l1-1-1.dll.so
%{lib32dir}/wine/ext-ms-win-ntuser-private-l1-1-1.dll.so
%{lib32dir}/wine/ext-ms-win-ntuser-rectangle-ext-l1-1-0.dll.so
%{lib32dir}/wine/ext-ms-win-ntuser-uicontext-ext-l1-1-0.dll.so
%{lib32dir}/wine/ext-ms-win-ntuser-window-l1-1-1.dll.so
%{lib32dir}/wine/ext-ms-win-rtcore-gdi-object-l1-1-0.dll.so
%{lib32dir}/wine/ext-ms-win-rtcore-gdi-rgn-l1-1-0.dll.so
%{lib32dir}/wine/ext-ms-win-rtcore-ntuser-dc-access-l1-1-0.dll.so
%{lib32dir}/wine/ext-ms-win-rtcore-ntuser-dpi-l1-1-0.dll.so
%{lib32dir}/wine/ext-ms-win-rtcore-ntuser-sysparams-l1-1-0.dll.so
%{lib32dir}/wine/extrac32.exe.so
%{lib32dir}/wine/faultrep.dll.so
%{lib32dir}/wine/findstr.exe.so
%{lib32dir}/wine/fltlib.dll.so
%{lib32dir}/wine/fltmgr.sys.so
%{lib32dir}/wine/fntcache.dll.so
%{lib32dir}/wine/fontsub.dll.so
%{lib32dir}/wine/fsutil.exe.so
%{lib32dir}/wine/fusion.dll.so
%{lib32dir}/wine/fwpuclnt.dll.so
%{lib32dir}/wine/gameux.dll.so
%{lib32dir}/wine/gdi.exe16.so
%{lib32dir}/wine/gdi32.dll.so
%{lib32dir}/wine/gdiplus.dll.so
%{lib32dir}/wine/glu32.dll.so
%{lib32dir}/wine/gphoto2.ds.so
%{lib32dir}/wine/gpkcsp.dll.so
%{lib32dir}/wine/hal.dll.so
%{lib32dir}/wine/hh.exe.so
%{lib32dir}/wine/hhctrl.ocx.so
%{lib32dir}/wine/hid.dll.so
%{lib32dir}/wine/hidclass.sys.so
%{lib32dir}/wine/hlink.dll.so
%{lib32dir}/wine/hnetcfg.dll.so
%{lib32dir}/wine/hostname.exe.so
%{lib32dir}/wine/httpapi.dll.so
%{lib32dir}/wine/icacls.exe.so
%{lib32dir}/wine/iccvid.dll.so
%{lib32dir}/wine/icinfo.exe.so
%{lib32dir}/wine/icmp.dll.so
%{lib32dir}/wine/ieframe.dll.so
%{lib32dir}/wine/iexplore.exe.so
%{lib32dir}/wine/ifsmgr.vxd.so
%{lib32dir}/wine/imaadp32.acm.so
%{lib32dir}/wine/imagehlp.dll.so
%{lib32dir}/wine/imm.dll16.so
%{lib32dir}/wine/imm32.dll.so
%{lib32dir}/wine/inetcomm.dll.so
%{lib32dir}/wine/inetcpl.cpl.so
%{lib32dir}/wine/inetmib1.dll.so
%{lib32dir}/wine/infosoft.dll.so
%{lib32dir}/wine/initpki.dll.so
%{lib32dir}/wine/inkobj.dll.so
%{lib32dir}/wine/inseng.dll.so
%{lib32dir}/wine/ipconfig.exe.so
%{lib32dir}/wine/iphlpapi.dll.so
%{lib32dir}/wine/iprop.dll.so
%{lib32dir}/wine/irprops.cpl.so
%{lib32dir}/wine/itircl.dll.so
%{lib32dir}/wine/itss.dll.so
%{lib32dir}/wine/joy.cpl.so
%{lib32dir}/wine/jscript.dll.so
%{lib32dir}/wine/jsproxy.dll.so
%{lib32dir}/wine/kernel32.dll.so
%{lib32dir}/wine/kernelbase.dll.so
%{lib32dir}/wine/keyboard.drv16.so
%{lib32dir}/wine/krnl386.exe16.so
%{lib32dir}/wine/ksuser.dll.so
%{lib32dir}/wine/ktmw32.dll.so
%{lib32dir}/wine/loadperf.dll.so
%{lib32dir}/wine/localspl.dll.so
%{lib32dir}/wine/localui.dll.so
%{lib32dir}/wine/lodctr.exe.so
%{lib32dir}/wine/lz32.dll.so
%{lib32dir}/wine/lzexpand.dll16.so
%{lib32dir}/wine/mapi32.dll.so
%{lib32dir}/wine/mapistub.dll.so
%{lib32dir}/wine/mciavi32.dll.so
%{lib32dir}/wine/mcicda.dll.so
%{lib32dir}/wine/mciqtz32.dll.so
%{lib32dir}/wine/mciseq.dll.so
%{lib32dir}/wine/mciwave.dll.so
%{lib32dir}/wine/mf.dll.so
%{lib32dir}/wine/mf3216.dll.so
%{lib32dir}/wine/mfplat.dll.so
%{lib32dir}/wine/mfreadwrite.dll.so
%{lib32dir}/wine/mgmtapi.dll.so
%{lib32dir}/wine/midimap.dll.so
%{lib32dir}/wine/mlang.dll.so
%{lib32dir}/wine/mmcndmgr.dll.so
%{lib32dir}/wine/mmdevapi.dll.so
%{lib32dir}/wine/mmdevldr.vxd.so
%{lib32dir}/wine/mmsystem.dll16.so
%{lib32dir}/wine/mofcomp.exe.so
%{lib32dir}/wine/monodebg.vxd.so
%{lib32dir}/wine/mountmgr.sys.so
%{lib32dir}/wine/mouse.drv16.so
%{lib32dir}/wine/mpr.dll.so
%{lib32dir}/wine/mprapi.dll.so
%{lib32dir}/wine/msacm.dll16.so
%{lib32dir}/wine/msacm32.dll.so
%{lib32dir}/wine/msacm32.drv.so
%{lib32dir}/wine/msadp32.acm.so
%{lib32dir}/wine/msasn1.dll.so
%{lib32dir}/wine/mscat32.dll.so
%{lib32dir}/wine/mscms.dll.so
%{lib32dir}/wine/mscoree.dll.so
%{lib32dir}/wine/msctf.dll.so
%{lib32dir}/wine/msctfp.dll.so
%{lib32dir}/wine/msdaps.dll.so
%{lib32dir}/wine/msdelta.dll.so
%{lib32dir}/wine/msdmo.dll.so
%{lib32dir}/wine/msdrm.dll.so
%{lib32dir}/wine/msftedit.dll.so
%{lib32dir}/wine/msg711.acm.so
%{lib32dir}/wine/msgsm32.acm.so
%{lib32dir}/wine/mshta.exe.so
%{lib32dir}/wine/mshtml.dll.so
%{lib32dir}/wine/mshtml.tlb.so
%{lib32dir}/wine/msi.dll.so
%{lib32dir}/wine/msident.dll.so
%{lib32dir}/wine/msiexec.exe.so
%{lib32dir}/wine/msimg32.dll.so
%{lib32dir}/wine/msimsg.dll.so
%{lib32dir}/wine/msimtf.dll.so
%{lib32dir}/wine/msinfo32.exe.so
%{lib32dir}/wine/msisip.dll.so
%{lib32dir}/wine/msisys.ocx.so
%{lib32dir}/wine/msls31.dll.so
%{lib32dir}/wine/msnet32.dll.so
%{lib32dir}/wine/mspatcha.dll.so
%{lib32dir}/wine/msports.dll.so
%{lib32dir}/wine/msrle32.dll.so
%{lib32dir}/wine/msscript.ocx.so
%{lib32dir}/wine/mssign32.dll.so
%{lib32dir}/wine/mssip32.dll.so
%{lib32dir}/wine/mstask.dll.so
%{lib32dir}/wine/msvcirt.dll.so
%{lib32dir}/wine/msvcm80.dll.so
%{lib32dir}/wine/msvcm90.dll.so
%{lib32dir}/wine/msvcp100.dll.so
%{lib32dir}/wine/msvcp110.dll.so
%{lib32dir}/wine/msvcp120.dll.so
%{lib32dir}/wine/msvcp120_app.dll.so
%{lib32dir}/wine/msvcp140.dll.so
%{lib32dir}/wine/msvcp60.dll.so
%{lib32dir}/wine/msvcp70.dll.so
%{lib32dir}/wine/msvcp71.dll.so
%{lib32dir}/wine/msvcp80.dll.so
%{lib32dir}/wine/msvcp90.dll.so
%{lib32dir}/wine/msvcr100.dll.so
%{lib32dir}/wine/msvcr110.dll.so
%{lib32dir}/wine/msvcr120.dll.so
%{lib32dir}/wine/msvcr120_app.dll.so
%{lib32dir}/wine/msvcr70.dll.so
%{lib32dir}/wine/msvcr71.dll.so
%{lib32dir}/wine/msvcr80.dll.so
%{lib32dir}/wine/msvcr90.dll.so
%{lib32dir}/wine/msvcrt.dll.so
%{lib32dir}/wine/msvcrt20.dll.so
%{lib32dir}/wine/msvcrt40.dll.so
%{lib32dir}/wine/msvcrtd.dll.so
%{lib32dir}/wine/msvfw32.dll.so
%{lib32dir}/wine/msvidc32.dll.so
%{lib32dir}/wine/msvideo.dll16.so
%{lib32dir}/wine/mswsock.dll.so
%{lib32dir}/wine/msxml.dll.so
%{lib32dir}/wine/msxml2.dll.so
%{lib32dir}/wine/msxml3.dll.so
%{lib32dir}/wine/msxml4.dll.so
%{lib32dir}/wine/msxml6.dll.so
%{lib32dir}/wine/mtxdm.dll.so
%{lib32dir}/wine/ncrypt.dll.so
%{lib32dir}/wine/nddeapi.dll.so
%{lib32dir}/wine/ndis.sys.so
%{lib32dir}/wine/net.exe.so
%{lib32dir}/wine/netapi32.dll.so
%{lib32dir}/wine/netcfgx.dll.so
%{lib32dir}/wine/netprofm.dll.so
%{lib32dir}/wine/netsh.exe.so
%{lib32dir}/wine/netstat.exe.so
%{lib32dir}/wine/newdev.dll.so
%{lib32dir}/wine/ngen.exe.so
%{lib32dir}/wine/normaliz.dll.so
%{lib32dir}/wine/notepad.exe.so
%{lib32dir}/wine/npmshtml.dll.so
%{lib32dir}/wine/npptools.dll.so
%{lib32dir}/wine/ntdll.dll.so
%{lib32dir}/wine/ntdsapi.dll.so
%{lib32dir}/wine/ntoskrnl.exe.so
%{lib32dir}/wine/ntprint.dll.so
%{lib32dir}/wine/objsel.dll.so
%{lib32dir}/wine/odbc32.dll.so
%{lib32dir}/wine/odbccp32.dll.so
%{lib32dir}/wine/odbccu32.dll.so
%{lib32dir}/wine/ole2.dll16.so
%{lib32dir}/wine/ole2conv.dll16.so
%{lib32dir}/wine/ole2disp.dll16.so
%{lib32dir}/wine/ole2nls.dll16.so
%{lib32dir}/wine/ole2prox.dll16.so
%{lib32dir}/wine/ole2thk.dll16.so
%{lib32dir}/wine/ole32.dll.so
%{lib32dir}/wine/oleacc.dll.so
%{lib32dir}/wine/oleaut32.dll.so
%{lib32dir}/wine/olecli.dll16.so
%{lib32dir}/wine/olecli32.dll.so
%{lib32dir}/wine/oledb32.dll.so
%{lib32dir}/wine/oledlg.dll.so
%{lib32dir}/wine/olepro32.dll.so
%{lib32dir}/wine/olesvr.dll16.so
%{lib32dir}/wine/olesvr32.dll.so
%{lib32dir}/wine/olethk32.dll.so
%{lib32dir}/wine/oleview.exe.so
%{lib32dir}/wine/opengl32.dll.so
%{lib32dir}/wine/packager.dll.so
%{lib32dir}/wine/pdh.dll.so
%{lib32dir}/wine/photometadatahandler.dll.so
%{lib32dir}/wine/pidgen.dll.so
%{lib32dir}/wine/ping.exe.so
%{lib32dir}/wine/plugplay.exe.so
%{lib32dir}/wine/powrprof.dll.so
%{lib32dir}/wine/presentationfontcache.exe.so
%{lib32dir}/wine/printui.dll.so
%{lib32dir}/wine/prntvpt.dll.so
%{lib32dir}/wine/progman.exe.so
%{lib32dir}/wine/propsys.dll.so
%{lib32dir}/wine/psapi.dll.so
%{lib32dir}/wine/pstorec.dll.so
%{lib32dir}/wine/qcap.dll.so
%{lib32dir}/wine/qedit.dll.so
%{lib32dir}/wine/qmgr.dll.so
%{lib32dir}/wine/qmgrprxy.dll.so
%{lib32dir}/wine/quartz.dll.so
%{lib32dir}/wine/query.dll.so
%{lib32dir}/wine/rasapi16.dll16.so
%{lib32dir}/wine/rasapi32.dll.so
%{lib32dir}/wine/rasdlg.dll.so
%{lib32dir}/wine/reg.exe.so
%{lib32dir}/wine/regapi.dll.so
%{lib32dir}/wine/regasm.exe.so
%{lib32dir}/wine/regedit.exe.so
%{lib32dir}/wine/regsvcs.exe.so
%{lib32dir}/wine/regsvr32.exe.so
%{lib32dir}/wine/resutils.dll.so
%{lib32dir}/wine/riched20.dll.so
%{lib32dir}/wine/riched32.dll.so
%{lib32dir}/wine/rpcrt4.dll.so
%{lib32dir}/wine/rpcss.exe.so
%{lib32dir}/wine/rsabase.dll.so
%{lib32dir}/wine/rsaenh.dll.so
%{lib32dir}/wine/rstrtmgr.dll.so
%{lib32dir}/wine/rtutils.dll.so
%{lib32dir}/wine/rundll.exe16.so
%{lib32dir}/wine/rundll32.exe.so
%{lib32dir}/wine/samlib.dll.so
%{lib32dir}/wine/sane.ds.so
%{lib32dir}/wine/sc.exe.so
%{lib32dir}/wine/scarddlg.dll.so
%{lib32dir}/wine/sccbase.dll.so
%{lib32dir}/wine/schannel.dll.so
%{lib32dir}/wine/schedsvc.dll.so
%{lib32dir}/wine/schtasks.exe.so
%{lib32dir}/wine/scrobj.dll.so
%{lib32dir}/wine/scrrun.dll.so
%{lib32dir}/wine/scsiport.sys.so
%{lib32dir}/wine/sdbinst.exe.so
%{lib32dir}/wine/secedit.exe.so
%{lib32dir}/wine/secur32.dll.so
%{lib32dir}/wine/security.dll.so
%{lib32dir}/wine/sensapi.dll.so
%{lib32dir}/wine/serialui.dll.so
%{lib32dir}/wine/servicemodelreg.exe.so
%{lib32dir}/wine/services.exe.so
%{lib32dir}/wine/setupapi.dll.so
%{lib32dir}/wine/setupx.dll16.so
%{lib32dir}/wine/sfc.dll.so
%{lib32dir}/wine/sfc_os.dll.so
%{lib32dir}/wine/shdoclc.dll.so
%{lib32dir}/wine/shdocvw.dll.so
%{lib32dir}/wine/shell.dll16.so
%{lib32dir}/wine/shell32.dll.so
%{lib32dir}/wine/shfolder.dll.so
%{lib32dir}/wine/shlwapi.dll.so
%{lib32dir}/wine/shutdown.exe.so
%{lib32dir}/wine/slbcsp.dll.so
%{lib32dir}/wine/slc.dll.so
%{lib32dir}/wine/snmpapi.dll.so
%{lib32dir}/wine/softpub.dll.so
%{lib32dir}/wine/sound.drv16.so
%{lib32dir}/wine/spoolss.dll.so
%{lib32dir}/wine/spoolsv.exe.so
%{lib32dir}/wine/sspicli.dll.so
%{lib32dir}/wine/start.exe.so
%{lib32dir}/wine/stdole2.tlb.so
%{lib32dir}/wine/stdole32.tlb.so
%{lib32dir}/wine/sti.dll.so
%{lib32dir}/wine/storage.dll16.so
%{lib32dir}/wine/stress.dll16.so
%{lib32dir}/wine/subst.exe.so
%{lib32dir}/wine/svchost.exe.so
%{lib32dir}/wine/svrapi.dll.so
%{lib32dir}/wine/sxs.dll.so
%{lib32dir}/wine/system.drv16.so
%{lib32dir}/wine/systeminfo.exe.so
%{lib32dir}/wine/t2embed.dll.so
%{lib32dir}/wine/tapi32.dll.so
%{lib32dir}/wine/taskkill.exe.so
%{lib32dir}/wine/tasklist.exe.so
%{lib32dir}/wine/taskmgr.exe.so
%{lib32dir}/wine/taskschd.dll.so
%{lib32dir}/wine/tdh.dll.so
%{lib32dir}/wine/tdi.sys.so
%{lib32dir}/wine/termsv.exe.so
%{lib32dir}/wine/toolhelp.dll16.so
%{lib32dir}/wine/traffic.dll.so
%{lib32dir}/wine/twain.dll16.so
%{lib32dir}/wine/twain_32.dll.so
%{lib32dir}/wine/typelib.dll16.so
%{lib32dir}/wine/ucrtbase.dll.so
%{lib32dir}/wine/uiautomationcore.dll.so
%{lib32dir}/wine/unicows.dll.so
%{lib32dir}/wine/uninstaller.exe.so
%{lib32dir}/wine/unlodctr.exe.so
%{lib32dir}/wine/updspapi.dll.so
%{lib32dir}/wine/url.dll.so
%{lib32dir}/wine/urlmon.dll.so
%{lib32dir}/wine/usbd.sys.so
%{lib32dir}/wine/user.exe16.so
%{lib32dir}/wine/user32.dll.so
%{lib32dir}/wine/userenv.dll.so
%{lib32dir}/wine/usp10.dll.so
%{lib32dir}/wine/uxtheme.dll.so
%{lib32dir}/wine/vbscript.dll.so
%{lib32dir}/wine/vcomp.dll.so
%{lib32dir}/wine/vcomp100.dll.so
%{lib32dir}/wine/vcomp110.dll.so
%{lib32dir}/wine/vcomp120.dll.so
%{lib32dir}/wine/vcomp140.dll.so
%{lib32dir}/wine/vcomp90.dll.so
%{lib32dir}/wine/vcruntime140.dll.so
%{lib32dir}/wine/vdhcp.vxd.so
%{lib32dir}/wine/vdmdbg.dll.so
%{lib32dir}/wine/ver.dll16.so
%{lib32dir}/wine/version.dll.so
%{lib32dir}/wine/view.exe.so
%{lib32dir}/wine/virtdisk.dll.so
%{lib32dir}/wine/vmm.vxd.so
%{lib32dir}/wine/vnbt.vxd.so
%{lib32dir}/wine/vnetbios.vxd.so
%{lib32dir}/wine/vssapi.dll.so
%{lib32dir}/wine/vtdapi.vxd.so
%{lib32dir}/wine/vwin32.vxd.so
%{lib32dir}/wine/w32skrnl.dll.so
%{lib32dir}/wine/w32sys.dll16.so
%{lib32dir}/wine/wbemdisp.dll.so
%{lib32dir}/wine/wbemprox.dll.so
%{lib32dir}/wine/webservices.dll.so
%{lib32dir}/wine/wer.dll.so
%{lib32dir}/wine/wevtapi.dll.so
%{lib32dir}/wine/wevtutil.exe.so
%{lib32dir}/wine/wiaservc.dll.so
%{lib32dir}/wine/wimgapi.dll.so
%{lib32dir}/wine/win32s16.dll16.so
%{lib32dir}/wine/win87em.dll16.so
%{lib32dir}/wine/winaspi.dll16.so
%{lib32dir}/wine/windebug.dll16.so
%{lib32dir}/wine/windowscodecs.dll.so
%{lib32dir}/wine/windowscodecsext.dll.so
%{lib32dir}/wine/winealsa.drv.so
%{lib32dir}/wine/wineboot.exe.so
%{lib32dir}/wine/winebrowser.exe.so
%{lib32dir}/wine/winebus.sys.so
%{lib32dir}/wine/winecfg.exe.so
%{lib32dir}/wine/wineconsole.exe.so
%{lib32dir}/wine/wined3d.dll.so
%{lib32dir}/wine/winedbg.exe.so
%{lib32dir}/wine/winedevice.exe.so
%{lib32dir}/wine/winefile.exe.so
%{lib32dir}/wine/winegstreamer.dll.so
%{lib32dir}/wine/winehid.sys.so
%{lib32dir}/wine/winejoystick.drv.so
%{lib32dir}/wine/winemapi.dll.so
%{lib32dir}/wine/winemenubuilder.exe.so
%{lib32dir}/wine/winemine.exe.so
%{lib32dir}/wine/winemsibuilder.exe.so
%{lib32dir}/wine/winepath.exe.so
%{lib32dir}/wine/wineps.drv.so
%{lib32dir}/wine/wineps16.drv16.so
%{lib32dir}/wine/winepulse.drv.so
%{lib32dir}/wine/winevdm.exe.so
%{lib32dir}/wine/winex11.drv.so
%{lib32dir}/wine/wing.dll16.so
%{lib32dir}/wine/wing32.dll.so
%{lib32dir}/wine/winhelp.exe16.so
%{lib32dir}/wine/winhlp32.exe.so
%{lib32dir}/wine/winhttp.dll.so
%{lib32dir}/wine/wininet.dll.so
%{lib32dir}/wine/winmm.dll.so
%{lib32dir}/wine/winnls.dll16.so
%{lib32dir}/wine/winnls32.dll.so
%{lib32dir}/wine/winoldap.mod16.so
%{lib32dir}/wine/winscard.dll.so
%{lib32dir}/wine/winsock.dll16.so
%{lib32dir}/wine/winspool.drv.so
%{lib32dir}/wine/winsta.dll.so
%{lib32dir}/wine/wintab.dll16.so
%{lib32dir}/wine/wintab32.dll.so
%{lib32dir}/wine/wintrust.dll.so
%{lib32dir}/wine/winusb.dll.so
%{lib32dir}/wine/winver.exe.so
%{lib32dir}/wine/wlanapi.dll.so
%{lib32dir}/wine/wldap32.dll.so
%{lib32dir}/wine/wmasf.dll.so
%{lib32dir}/wine/wmi.dll.so
%{lib32dir}/wine/wmic.exe.so
%{lib32dir}/wine/wmiutils.dll.so
%{lib32dir}/wine/wmp.dll.so
%{lib32dir}/wine/wmplayer.exe.so
%{lib32dir}/wine/wmvcore.dll.so
%{lib32dir}/wine/wnaspi32.dll.so
%{lib32dir}/wine/wordpad.exe.so
%{lib32dir}/wine/wow32.dll.so
%{lib32dir}/wine/wpc.dll.so
%{lib32dir}/wine/wpcap.dll.so
%{lib32dir}/wine/write.exe.so
%{lib32dir}/wine/ws2_32.dll.so
%{lib32dir}/wine/wscript.exe.so
%{lib32dir}/wine/wsdapi.dll.so
%{lib32dir}/wine/wshom.ocx.so
%{lib32dir}/wine/wsnmp32.dll.so
%{lib32dir}/wine/wsock32.dll.so
%{lib32dir}/wine/wtsapi32.dll.so
%{lib32dir}/wine/wuapi.dll.so
%{lib32dir}/wine/wuaueng.dll.so
%{lib32dir}/wine/wusa.exe.so
%{lib32dir}/wine/xcopy.exe.so
%{lib32dir}/wine/xinput1_1.dll.so
%{lib32dir}/wine/xinput1_2.dll.so
%{lib32dir}/wine/xinput1_3.dll.so
%{lib32dir}/wine/xinput1_4.dll.so
%{lib32dir}/wine/xinput9_1_0.dll.so
%{lib32dir}/wine/xmllite.dll.so
%{lib32dir}/wine/xolehlp.dll.so
%{lib32dir}/wine/xpsprint.dll.so
%{lib32dir}/wine/xpssvcs.dll.so

%if %{with staging}
%{lib32dir}/wine/api-ms-win-core-heap-l2-1-0.dll.so
%{lib32dir}/wine/api-ms-win-core-shlwapi-obsolete-l1-2-0.dll.so
%{lib32dir}/wine/api-ms-win-rtcore-ntuser-draw-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-rtcore-ntuser-window-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-shcore-obsolete-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-shcore-stream-l1-1-0.dll.so
%{lib32dir}/wine/api-ms-win-shcore-thread-l1-1-0.dll.so
%{lib32dir}/wine/dxgkrnl.sys.so
%{lib32dir}/wine/dxgmms1.sys.so
%{lib32dir}/wine/ext-ms-win-appmodel-usercontext-l1-1-0.dll.so
%{lib32dir}/wine/ext-ms-win-ntuser-mouse-l1-1-0.dll.so
%{lib32dir}/wine/ext-ms-win-rtcore-ntuser-syscolors-l1-1-0.dll.so
%{lib32dir}/wine/ext-ms-win-uxtheme-themes-l1-1-0.dll.so
%{lib32dir}/wine/ext-ms-win-xaml-pal-l1-1-0.dll.so
%{lib32dir}/wine/feclient.dll.so
%{lib32dir}/wine/iertutil.dll.so
%{lib32dir}/wine/msidb.exe.so
%{lib32dir}/wine/nvapi.dll.so
%{lib32dir}/wine/nvcuda.dll.so
%{lib32dir}/wine/nvcuvid.dll.so
%{lib32dir}/wine/nvencodeapi.dll.so
%{lib32dir}/wine/shcore.dll.so
%{lib32dir}/wine/uxtheme-gtk.dll.so
%{lib32dir}/wine/vulkan-1.dll.so
%{lib32dir}/wine/vulkan.dll.so
%{lib32dir}/wine/win32k.sys.so
%{lib32dir}/wine/wined3d-csmt.dll.so
%{lib32dir}/wine/wuauserv.exe.so
%endif

%if %{with mpg123}
%{lib32dir}/wine/winemp3.acm.so
%endif

%if %{with opencl}
%{lib32dir}/wine/opencl.dll.so
%endif

%if %{with openal}
%{lib32dir}/wine/openal32.dll.so
%{lib32dir}/wine/x3daudio1_0.dll.so
%{lib32dir}/wine/x3daudio1_1.dll.so
%{lib32dir}/wine/x3daudio1_2.dll.so
%{lib32dir}/wine/x3daudio1_3.dll.so
%{lib32dir}/wine/x3daudio1_4.dll.so
%{lib32dir}/wine/x3daudio1_5.dll.so
%{lib32dir}/wine/x3daudio1_6.dll.so
%{lib32dir}/wine/x3daudio1_7.dll.so
%{lib32dir}/wine/xapofx1_1.dll.so
%{lib32dir}/wine/xapofx1_2.dll.so
%{lib32dir}/wine/xapofx1_3.dll.so
%{lib32dir}/wine/xapofx1_4.dll.so
%{lib32dir}/wine/xapofx1_5.dll.so
%{lib32dir}/wine/xaudio2_0.dll.so
%{lib32dir}/wine/xaudio2_1.dll.so
%{lib32dir}/wine/xaudio2_2.dll.so
%{lib32dir}/wine/xaudio2_3.dll.so
%{lib32dir}/wine/xaudio2_4.dll.so
%{lib32dir}/wine/xaudio2_5.dll.so
%{lib32dir}/wine/xaudio2_6.dll.so
%{lib32dir}/wine/xaudio2_7.dll.so
%{lib32dir}/wine/xaudio2_8.dll.so
%{lib32dir}/wine/xaudio2_9.dll.so
%endif
# }}}
%{lib32dir}/wine/fakedlls/
%endif

%{_datadir}/applications/wine.desktop
%{_datadir}/wine/
# Man pages {{{
%{_mandir}/man1/msiexec.1*
%{_mandir}/man1/notepad.1*
%{_mandir}/man1/regedit.1*
%{_mandir}/man1/regsvr32.1*
%{_mandir}/man1/wine.1*
%{_mandir}/man1/wineboot.1*
%{_mandir}/man1/winecfg.1*
%{_mandir}/man1/wineconsole.1*
%{_mandir}/man1/winedbg.1*
%{_mandir}/man1/winedump.1*
%{_mandir}/man1/winefile.1*
%{_mandir}/man1/winemine.1*
%{_mandir}/man1/winepath.1*
%{_mandir}/man1/wineserver.1*
%lang(de) %{_mandir}/de.UTF-8/man1/wine.1*
%lang(de) %{_mandir}/de.UTF-8/man1/wineserver.1*
%lang(fr) %{_mandir}/fr.UTF-8/man1/wine.1*
%lang(fr) %{_mandir}/fr.UTF-8/man1/wineserver.1*
%lang(pl) %{_mandir}/pl.UTF-8/man1/wine.1*
# }}}

%files devel
# Binaries {{{
%{_bindir}/function_grep.pl
%{_bindir}/widl
%{_bindir}/winebuild
%{_bindir}/winecpp
%{_bindir}/wineg++
%{_bindir}/winegcc
%{_bindir}/winemaker
%{_bindir}/wmc
%{_bindir}/wrc
# }}}
%{_includedir}/wine/
%{_libdir}/libwine.so
%{_libdir}/wine/*.a
%{_libdir}/wine/*.def

%ifarch x86_64
%{lib32dir}/libwine.so
%{lib32dir}/wine/*.a
%{lib32dir}/wine/*.def
%endif

# Man pages {{{
%{_mandir}/man1/widl.1*
%{_mandir}/man1/winebuild.1*
%{_mandir}/man1/winecpp.1*
%{_mandir}/man1/wineg++.1*
%{_mandir}/man1/winegcc.1*
%{_mandir}/man1/winemaker.1*
%{_mandir}/man1/wmc.1*
%{_mandir}/man1/wrc.1*
%lang(de) %{_mandir}/de.UTF-8/man1/winemaker.1*
%lang(fr) %{_mandir}/fr.UTF-8/man1/winemaker.1*
# }}}


%changelog
* Wed Jun 28 2017 Jajauma's Packages <jajauma@yandex.ru> - 2:2.11-1
- Update to latest upstream release
- Package new libraries (api-ms-win-core-crt-l1-1-0.dll.so,
  api-ms-win-core-crt-l2-1-0.dll.so,
  api-ms-win-security-credentials-l1-1-0.dll.so)

* Sun Jun 11 2017 Jajauma's Packages <jajauma@yandex.ru> - 2:2.10-1
- Update to latest upstream release

* Sat Jun 03 2017 Jajauma's Packages <jajauma@yandex.ru> - 2:2.9-1
- Initial release

# vim: foldmethod=marker
