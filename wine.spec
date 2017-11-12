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
Version:        2.18
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
BuildRequires:  libXdamage-devel%{?_isa}
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
BuildRequires:  at-spi2-atk-devel%{?_isa}
BuildRequires:  gtk3-devel%{?_isa}
BuildRequires:  libva-devel%{?_isa}
BuildRequires:  pango-devel%{?_isa}
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
BuildRequires:  libXdamage-devel(x86-32)
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
BuildRequires:  at-spi2-atk-devel(x86-32)
BuildRequires:  gtk3-devel(x86-32)
BuildRequires:  libva-devel(x86-32)
BuildRequires:  pango-devel(x86-32)
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

pushd wine64-build
# Export some of distribution factory compiler flags manually. Exporting
# -D_FORTIFY_SOURCE=2 issues some (non-fatal) complaints so let's better hide
# it from the build system.
export CFLAGS="$(echo %{optflags} | sed -e 's/-Wp,-D_FORTIFY_SOURCE=2//')"
export LDFLAGS="%{__global_ldflags}"
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
# Avoid exporting any machine flags as those would break side-by-side WoW64
# building and also hide distribution _FORTIFY_SOURCE.
export CFLAGS="$(echo %{__global_cflags} | sed -e 's/-Wp,-D_FORTIFY_SOURCE=2//')"
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
# No _FORTIFY_SOURCE redefinition complaints and rely on distribution flags
# otherwise as much as possible
export CFLAGS="$(echo %{optflags} | sed -e 's/-Wp,-D_FORTIFY_SOURCE=2//')"
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
%{_bindir}/msiexec
%{_bindir}/notepad
%{_bindir}/regedit
%{_bindir}/regsvr32
%{_bindir}/wine
%{_bindir}/wine-preloader
%ifarch x86_64
%{_bindir}/wine64
%{_bindir}/wine64-preloader
%endif
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
%{_libdir}/libwine.so.*
%dir %{_libdir}/wine/
%{_libdir}/wine/*.so
%{_libdir}/wine/fakedlls/
%ifarch x86_64
%{lib32dir}/libwine.so.*
%dir %{lib32dir}/wine/
%{lib32dir}/wine/*.so
%{lib32dir}/wine/fakedlls/
%endif
%{_datadir}/applications/wine.desktop
%{_datadir}/wine/
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

%files devel
%{_bindir}/function_grep.pl
%{_bindir}/widl
%{_bindir}/winebuild
%{_bindir}/winecpp
%{_bindir}/wineg++
%{_bindir}/winegcc
%{_bindir}/winemaker
%{_bindir}/wmc
%{_bindir}/wrc
%{_includedir}/wine/
%{_libdir}/libwine.so
%{_libdir}/wine/*.a
%{_libdir}/wine/*.def
%ifarch x86_64
%{lib32dir}/libwine.so
%{lib32dir}/wine/*.a
%{lib32dir}/wine/*.def
%endif
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


%changelog
* Sun Nov 12 2017 Jajauma's Packages <jajauma@yandex.ru> - 2:2.18-1
- Update to latest upstream release

* Sun Nov 12 2017 Jajauma's Packages <jajauma@yandex.ru> - 2:2.17-1
- Update to latest upstream release

* Sun Nov 12 2017 Jajauma's Packages <jajauma@yandex.ru> - 2:2.16-1
- Update to latest upstream release

* Sat Aug 26 2017 Jajauma's Packages <jajauma@yandex.ru> - 2:2.15-1
- Update to latest upstream release

* Sat Aug 12 2017 Jajauma's Packages <jajauma@yandex.ru> - 2:2.14-1
- Update to latest upstream release

* Sat Aug 12 2017 Jajauma's Packages <jajauma@yandex.ru> - 2:2.13-3
- Try to export as many distribution flags as possible

* Fri Aug 11 2017 Jajauma's Packages <jajauma@yandex.ru> - 2:2.13-2
- Require pango-devel for building
- Require libXdamage-devel for building
- Require at-spi2-atk-devel for building
- Fixes for i686 build

* Wed Jul 26 2017 Jajauma's Packages <jajauma@yandex.ru> - 2:2.13-1
- Update to latest upstream release

* Thu Jul 20 2017 Jajauma's Packages <jajauma@yandex.ru> - 2:2.12-2
- Fix broken Epoch (must be 2)

* Wed Jul 12 2017 Jajauma's Packages <jajauma@yandex.ru> - 1:2.12-1
- Update to latest upstream release

* Wed Jun 28 2017 Jajauma's Packages <jajauma@yandex.ru> - 2:2.11-1
- Update to latest upstream release
- Package new libraries (api-ms-win-core-crt-l1-1-0.dll.so,
  api-ms-win-core-crt-l2-1-0.dll.so,
  api-ms-win-security-credentials-l1-1-0.dll.so)

* Sun Jun 11 2017 Jajauma's Packages <jajauma@yandex.ru> - 2:2.10-1
- Update to latest upstream release

* Sat Jun 03 2017 Jajauma's Packages <jajauma@yandex.ru> - 2:2.9-1
- Initial release
