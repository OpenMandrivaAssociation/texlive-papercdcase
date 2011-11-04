# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/papercdcase
# catalog-date 2007-03-11 14:35:09 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-papercdcase
Version:	20070311
Release:	1
Summary:	Origami-style folding paper CD case
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/papercdcase
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/papercdcase.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/papercdcase.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/papercdcase.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package implements a LaTeX style file to produce origami-
style folding paper CD cases.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/papercdcase/papercdcase.sty
%doc %{_texmfdistdir}/doc/latex/papercdcase/example.tex
%doc %{_texmfdistdir}/doc/latex/papercdcase/interactive.tex
%doc %{_texmfdistdir}/doc/latex/papercdcase/papercdcase.pdf
#- source
%doc %{_texmfdistdir}/source/latex/papercdcase/papercdcase.dtx
%doc %{_texmfdistdir}/source/latex/papercdcase/papercdcase.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
