## START: Set by rpmautospec
## (rpmautospec version 0.2.6)
%define autorelease(e:s:pb:) %{?-p:0.}%{lua:
    release_number = 3;
    base_release_number = tonumber(rpm.expand("%{?-b*}%{!?-b:1}"));
    print(release_number + base_release_number - 1);
}%{?-e:.%{-e*}}%{?-s:.%{-s*}}%{?dist}
## END: Set by rpmautospec

# Generated by rust2rpm 21
%bcond_without check

%global crate alacritty

Name:           rust-%{crate}
Version:        0.11.0
Release:        %autorelease
Summary:        Fast, cross-platform, OpenGL terminal emulator

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            https://crates.io/crates/alacritty
Source:         %{crates_source}
Source1:        https://github.com/alacritty/alacritty/releases/download/v%{version}/Alacritty.desktop
Source2:        https://github.com/alacritty/alacritty/releases/download/v%{version}/Alacritty.svg
Source3:        https://github.com/alacritty/alacritty/releases/download/v%{version}/alacritty.yml
Source4:        https://github.com/alacritty/alacritty/releases/download/v%{version}/alacritty.bash
Source5:        https://github.com/alacritty/alacritty/releases/download/v%{version}/_alacritty
Source6:        https://github.com/alacritty/alacritty/releases/download/v%{version}/alacritty.fish
Source7:        https://github.com/alacritty/alacritty/releases/download/v%{version}/alacritty.1.gz
Source8:        https://github.com/alacritty/alacritty/releases/download/v%{version}/alacritty-msg.1.gz

# Initial patched metadata
# * drop windows- and mac OS-specific dependencies
Patch0:         alacritty-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
ExcludeArch:    s390x

BuildRequires:  desktop-file-utils
BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Fast, cross-platform, OpenGL terminal emulator.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# * ASL 2.0
# * ASL 2.0 and MIT
# * ASL 2.0 or Boost
# * ASL 2.0 or MIT
# * BSD
# * CC0
# * ISC
# * MIT
# * MIT or ASL 2.0
# * Unlicense or MIT
# * zlib
License:        ASL 2.0 and BSD and CC0 and ISC and MIT and zlib

# libwayland-egl is dlopened when running on a wayland compositor
Requires:       libwayland-egl

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE-APACHE
%doc README.md
%{_bindir}/alacritty
%dir %{_datadir}/%{crate}
%{_mandir}/man1/alacritty.1*
%{_mandir}/man1/alacritty-msg.1*
%{_datadir}/applications/Alacritty.desktop
%{_datadir}/pixmaps/Alacritty.svg
%{_datadir}/%{crate}/alacritty.yml
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/alacritty
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_alacritty
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/alacritty.fish

%prep
%autosetup -n %{crate}-%{version_no_tilde}
%cargo_prep

zcat %{SOURCE7} >alacritty.1
zcat %{SOURCE8} >alacritty-msg.1

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install
install -m644 %{SOURCE1} -pD %{buildroot}%{_datadir}/applications/Alacritty.desktop
install -m644 %{SOURCE2} -pD %{buildroot}%{_datadir}/pixmaps/Alacritty.svg
install -m644 %{SOURCE3} -pD %{buildroot}%{_datadir}/%{crate}/alacritty.yml
install -m644 %{SOURCE4} -pD %{buildroot}%{_datadir}/bash-completion/completions/alacritty
install -m644 %{SOURCE5} -pD %{buildroot}%{_datadir}/zsh/site-functions/_alacritty
install -m644 %{SOURCE6} -pD %{buildroot}%{_datadir}/fish/vendor_completions.d/alacritty.fish
install -m644 -pDt %{buildroot}%{_mandir}/man1/ alacritty.1
install -m644 -pDt %{buildroot}%{_mandir}/man1/ alacritty-msg.1

%if %{with check}
%check
desktop-file-validate %{buildroot}%{_datadir}/applications/Alacritty.desktop
%cargo_test -- -- --skip config_read_eof stdout --skip completions stdout
%endif

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 26 2022 Zbigniew JÄ™drzejewski-Szmek <zbyszek@in.waw.pl> 0.10.1-2
- Exclude s390x

* Fri Feb 25 2022 Zbigniew JÄ™drzejewski-Szmek <zbyszek@in.waw.pl> 0.10.1-1
- Version 0.10.1 (rhbz#2035604)

* Thu Feb 17 2022 Fabio Valentini <decathorpe@gmail.com> 0.9.0-4
- Add dependency on dlopened libwayland-egl

* Tue Feb 15 2022 Zbigniew JÄ™drzejewski-Szmek <zbyszek@in.waw.pl> 0.9.0-3
- Rebuild with package notes

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 04 2021 Fabio Valentini <decathorpe@gmail.com> 0.9.0-1
- Update to version 0.9.0; Fixes RHBZ#1989483

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 19 2021 Fabio Valentini <decathorpe@gmail.com> - 0.8.0-1
- Update to version 0.8.0.
- Fixes RHBZ#1962046

* Sat Feb 20 20:35:00 CET 2021 returntrip <stefano@figura.im> - 0.7.2-2
- Fixes RHZB#1929687

* Sat Feb 20 15:45:00 CET 2021 returntrip <stefano@figura.im> - 0.7.2-1
- Update to 0.7.2 (Fixes RHZB#1930981)

* Sat Feb 6 12:25:00 CET 2021 returntrip <stefano@figura.im> - 0.7.1-1
- Update to 0.7.1 (Fixes RHZB#1914242)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 28 13:27:02 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.6.0-2
- Rebuild

* Sun Nov 29 17:30:00 CEST 2020 returntrip <stefano@figura.im> - 0.6.0-1
- Update to 0.6.0

* Fri Oct 16 13:45:04 CEST 2020 returntrip <stefano@figura.im> - 0.5.0-1
- Initial package

