%define githash 2a2d38fcaa0c98262885681b901d67fea231bc50
%define releasenum 44


%define shorthash %(c=%{githash}; echo ${c:0:10})

Name:          alacritty
Version:       0.11.0
Release:       0.%{releasenum}.git.%{shorthash}%{?dist}
Summary:       A cross-platform, GPU enhanced terminal emulator
License:       ASL 2.0
URL:           https://github.com/alacritty/alacritty
VCS:           https://github.com/alacritty/alacritty.git
Source:        %{url}/archive/%{githash}/%{name}-%{githash}.tar.gz

BuildRequires: rust
BuildRequires: cargo
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: python3
BuildRequires: freetype-devel
BuildRequires: fontconfig-devel
BuildRequires: libxcb-devel
BuildRequires: desktop-file-utils
BuildRequires: ncurses

%description
Alacritty is a terminal emulator with a strong focus on simplicity and
performance. With such a strong focus on performance, included features are
carefully considered and you can always expect Alacritty to be blazingly fast.
By making sane choices for defaults, Alacritty requires no additional setup.
However, it does allow configuration of many aspects of the terminal.

%description -n %{crate} %{_description}
	
 
	
%files       -n alacritty
	
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
%autosetup -n alacritty-%{githash} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
	


%install
	
%cargo_install
install -p -D -m755 target/release/alacritty         %{buildroot}%{_bindir}/alacritty
install -p -D -m644 extra/linux/Alacritty.desktop    %{buildroot}%{_datadir}/applications/Alacritty.desktop
install -p -D -m644 extra/logo/alacritty-term.svg    %{buildroot}%{_datadir}/pixmaps/Alacritty.svg
install -p -D -m644 alacritty.yml                    %{buildroot}%{_datadir}/alacritty/alacritty.yml
tic     -xe alacritty-direct \
                    extra/alacritty.info       -o    %{buildroot}%{_datadir}/terminfo
install -p -D -m644 extra/completions/alacritty.bash %{buildroot}%{_datadir}/bash-completion/completions/alacritty
install -p -D -m644 extra/completions/_alacritty     %{buildroot}%{_datadir}/zsh/site-functions/_alacritty
install -p -D -m644 extra/completions/alacritty.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/alacritty.fish
install -p -D -m644 extra/alacritty.man              %{buildroot}%{_mandir}/man1/alacritty.1

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/Alacritty.desktop

%files
%{_bindir}/alacritty
%{_datadir}/applications/Alacritty.desktop
%{_datadir}/pixmaps/Alacritty.svg
%{_datadir}/alacritty/alacritty.yml
%{_datadir}/terminfo/a/alacritty-direct
%{_datadir}/bash-completion/completions/alacritty
%{_datadir}/zsh/site-functions/_alacritty
%{_datadir}/fish/vendor_completions.d/alacritty.fish
%{_mandir}/man1/alacritty.1*
