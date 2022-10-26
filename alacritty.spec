%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname alacritty

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        Fast, cross-platform, OpenGL terminal emulator

License:        ASL 2.0 or MIT
URL:            https://github.com/alacritty/alacritty
Source:         https://github.com/alacritty/alacritty/archive/master/alacritty-master.tar.gz

BuildRequires:  rust-packaging

%description
Fast, cross-platform, OpenGL terminal emulator.

%prep
%autosetup -n alacritty-master -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
