# Rust packages always list license files and docs
# inside the crate as well as the containing directory
%undefine _duplicate_files_terminate_build
# Avoid dependency on way too old version of quickcheck
%bcond_with check
%global debug_package %{nil}

%global crate byteorder

Name:           rust-byteorder
Version:        1.5.0
Release:        1
Summary:        Library for reading/writing numbers in big-endian and little-endian
Group:          Development/Rust

License:        Unlicense OR MIT
URL:            https://crates.io/crates/byteorder
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  rust >= 1.60
%if %{with check}
BuildRequires:  (crate(quickcheck) >= 0.9.2 with crate(quickcheck) < 0.10.0~)
BuildRequires:  (crate(rand/default) >= 0.7.0 with crate(rand/default) < 0.8.0~)
%endif

%global _description %{expand:
Library for reading/writing numbers in big-endian and little-endian.}

%description %{_description}

%package        devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(byteorder) = 1.5.0
Requires:       cargo
Requires:       rust >= 1.60

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/COPYING
%license %{crate_instdir}/LICENSE-MIT
%license %{crate_instdir}/UNLICENSE
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(byteorder/default) = 1.5.0
Requires:       cargo
Requires:       crate(byteorder) = 1.5.0
Requires:       crate(byteorder/std) = 1.5.0

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+i128-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(byteorder/i128) = 1.5.0
Requires:       cargo
Requires:       crate(byteorder) = 1.5.0

%description -n %{name}+i128-devel %{_description}

This package contains library source intended for building other packages which
use the "i128" feature of the "%{crate}" crate.

%files       -n %{name}+i128-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(byteorder/std) = 1.5.0
Requires:       cargo
Requires:       crate(byteorder) = 1.5.0

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
