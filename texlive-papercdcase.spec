# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/papercdcase
# catalog-date 2007-03-11 14:35:09 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-papercdcase
Version:	20070311
Release:	4
Summary:	Origami-style folding paper CD case
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/papercdcase
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/papercdcase.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/papercdcase.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/papercdcase.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package implements a LaTeX style file to produce origami-
style folding paper CD cases.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070311-2
+ Revision: 754638
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070311-1
+ Revision: 719186
- texlive-papercdcase
- texlive-papercdcase
- texlive-papercdcase
- texlive-papercdcase

